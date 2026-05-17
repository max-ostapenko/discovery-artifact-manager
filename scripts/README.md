# GCP API Insights Feed

This directory contains the scripts that turn discovery-document changes into
developer-readable Markdown insights under `feed/`.

The pipeline is intentionally split into small pieces:

1. `update_disco.py` refreshes watched discovery documents.
2. `open_pr.py` opens the normal discovery update PR.
3. `diff_to_feed.py` compares changed discovery JSON files, asks Gemini for one
   insight per changed API, and writes dated Markdown files to `feed/`.

The feed is the source of truth for now. Publishing is deliberately undecided:
the generated Markdown can later be imported into a website repo, copied into
LinkedIn drafts, or published through a dedicated workflow.

## Files

| File | Purpose |
|---|---|
| `diff_to_feed.py` | Orchestrates extraction, LLM analysis, and feed writing. |
| `diff_preprocessor.py` | Converts discovery JSON changes into structured `{added, removed, modified}` paths. |
| `llm_client.py` | Calls Gemini through Vertex AI using ADC/WIF. No API keys. |
| `feed_writer.py` | Writes per-API Markdown files and updates `feed/index.json`. |
| `prompts/api_change_analyst.txt` | System prompt for developer-impact analysis. |

## CI Flow

`.github/workflows/update-disco.yml` runs this process on the existing 5-hour
schedule:

1. Checkout with `fetch-depth: 2`, so `HEAD~1..HEAD` diffs are available.
2. Authenticate to Google Cloud with `google-github-actions/auth`.
3. Install `google-genai` and `google-auth`.
4. Run `python scripts/update_disco.py && python scripts/open_pr.py`.
5. Run `python scripts/diff_to_feed.py`.
6. Commit any new files under `feed/`.

Required GitHub secrets:

| Secret | Purpose |
|---|---|
| `GCP_WORKLOAD_IDENTITY_PROVIDER` | Workload Identity Federation provider for Google Cloud auth. |
| `GCP_SERVICE_ACCOUNT` | Service account used by the workflow. |

`GEMINI_API_KEY` is not used.

## Local Usage

Inspect the structured diff without calling Gemini or writing feed files:

```bash
python3 scripts/diff_to_feed.py --dry-run
```

Compare specific refs:

```bash
python3 scripts/diff_to_feed.py --dry-run --base abc1234 --head def5678
```

Run the full pipeline locally with Application Default Credentials:

```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
python3 scripts/diff_to_feed.py
```

Useful options:

| Option | Purpose |
|---|---|
| `--base REF` | Base git ref. Defaults to `HEAD~1`. |
| `--head REF` | Head git ref. Defaults to `HEAD`. |
| `--date YYYY-MM-DD` | Override the insight date used in filenames and frontmatter. |
| `--dry-run` | Print structured diffs only. Skips Gemini and feed writes. |
| `--log-level` | One of `DEBUG`, `INFO`, `WARNING`, `ERROR`. |

## Feed Output

`feed_writer.py` writes one Markdown file per API per insight date:

```text
feed/
  README.md
  index.json
  2026-04-17-dataform-v1.md
  2026-04-17-dataform-v1beta1.md
  2026-04-18-bigquery-v2.md
  2026-04-18-bigquery-v2_v2.md
```

If the same API gets multiple insights on the same date, the writer uses `_v2`,
`_v3`, and so on rather than overwriting earlier files.

`feed/index.json` is kept newest-first and records the published slug, API,
title, impact, tags, score, and generation timestamp. This is the hook for
future deduplication or website import.

## Filtering And Tuning

| Lever | Location |
|---|---|
| LLM model | `MODEL` in `llm_client.py` |
| Prompt, tone, scoring rules | `prompts/api_change_analyst.txt` |
| Interesting score threshold | `INTERESTING_SCORE_THRESHOLD` in `feed_writer.py` |
| Noise keys and path prefixes | `NOISE_KEYS` / `NOISE_PATH_PREFIXES` in `diff_preprocessor.py` |
| API watchlist | Existing logic in `update_disco.py` |

The current `INTERESTING_SCORE_THRESHOLD` is `2`. That is intentionally lenient
for early testing so we can review more samples before tightening signal.

## Early Testing Strategy

The safest early loop is:

1. Generate feed files from real diffs.
2. Review the Markdown for accuracy and usefulness.
3. Render or import a small sample into `../Github/website-source` as drafts.
4. Only after the quality bar is clear, adapt selected entries into LinkedIn
   posts or a publish workflow.

This keeps publishing separate from content validation. The artifact to trust
first is `feed/`, not a public channel.

## Tests

Run the same checks used by CI:

```bash
python3 -m black scripts/*.py tests/*.py --check
python3 -m mypy scripts/*.py tests/*.py
python3 -m unittest tests/*.py
```

Coverage currently includes:

- diff preprocessing for noise-only changes and `{added, removed, modified}`
  path extraction
- feed writing, same-day versioning, index updates, and low-score skipping

## Future Work

- Add a website import/publish path once the target channel is chosen.
- Use `feed/index.json` to suppress repetitive low-delta updates.
- Optionally generate LinkedIn-ready draft text from selected feed entries.
