"""
Thin client around the Gemini API for generating API change insights.

Uses the `google-genai` SDK with Vertex AI backend, authenticated via
Application Default Credentials (ADC). No API key required.

Local usage:
    gcloud auth application-default login
    gcloud config set project YOUR_PROJECT_ID

CI:
    Use google-github-actions/auth with Workload Identity Federation.
    The GCP project is auto-detected from the ADC environment.
"""

import json
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

PROMPT_PATH = Path(__file__).parent / "prompts" / "api_change_analyst.txt"
MODEL = "gemini-3-flash-preview"


def _load_system_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")


def _get_project_id() -> Optional[str]:
    """Resolve GCP project ID from env, ADC, or ADC JSON quota_project_id."""
    import os

    if project := os.getenv("GOOGLE_CLOUD_PROJECT") or os.getenv("GCLOUD_PROJECT"):
        return project
    try:
        import google.auth

        _, project = google.auth.default()
        if project:
            return project
    except Exception:
        pass
    # gcloud user credentials store the quota project in the ADC JSON file
    try:
        import json

        adc_path = os.path.expanduser(
            "~/.config/gcloud/application_default_credentials.json"
        )
        with open(adc_path) as f:
            data = json.load(f)
        if quota_project := data.get("quota_project_id"):
            return quota_project
    except Exception:
        pass
    return None


def analyze_api_diff(diff: dict) -> Optional[dict]:
    """Send a structured API diff to Gemini and return the parsed JSON insight.

    Uses Vertex AI backend (ADC with standard cloud-platform scope).

    Args:
        diff: Structured diff dict with keys: api, added, removed, modified.

    Returns:
        Parsed insight dict, or None if credentials are unavailable or the call fails.
    """
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        logger.error("google-genai not installed. Run: pip install google-genai")
        return None

    project = _get_project_id()
    if not project:
        logger.warning(
            "No GCP project found. Run: gcloud config set project YOUR_PROJECT_ID "
            "or set GOOGLE_CLOUD_PROJECT env var. Skipping LLM analysis."
        )
        return None

    try:
        client = genai.Client(vertexai=True, project=project, location="global")
    except Exception as e:
        logger.warning(f"Could not initialise Vertex AI client: {e}")
        return None

    system_prompt = _load_system_prompt()
    user_message = json.dumps(diff, indent=2)
    api_name = diff.get("api", "unknown")
    logger.info(f"Sending diff for {api_name} to Gemini ({MODEL}, Vertex AI) ...")

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json",
                temperature=0.3,
            ),
        )
        raw = (response.text or "").strip()
        result = json.loads(raw)
        logger.info(
            f"  → {result.get('api')}: score={result.get('interesting_score')}, "
            f"impact={result.get('impact')}, breaking={result.get('breaking')}"
        )
        return result
    except Exception as e:
        logger.error(f"Gemini call failed for {api_name}: {e}")
        return None
