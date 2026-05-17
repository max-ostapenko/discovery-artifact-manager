# GCP API Insights Feed

Auto-generated insights about changes to Google Cloud Platform APIs, sourced from the
Google Discovery Service and analysed by Gemini.

Each file covers one API for one update event. Filenames follow the pattern:
```
YYYY-MM-DD-{api-version}.md        # e.g. 2026-04-16-bigquery-v2.md
YYYY-MM-DD-{api-version}_v2.md     # if the same API updated twice in one day
```

## index.json

`index.json` is a machine-readable manifest of all published insights, sorted newest-first.
It's designed to support future deduplication (e.g., consolidating sequential partial updates
to the same API) and enhancement (e.g., enriching old posts when context accumulates).

## How it works

1. The `update-disco.yml` CI fetches fresh discovery documents every 5 hours
2. Changed files are pre-processed into structured `{added, removed, modified}` path diffs — noise keys like `revision` and `etag` are stripped
3. Each changed API's diff is sent to Gemini with a tailored analyst prompt
4. Insights scoring below `interesting_score = 4` are silently dropped
5. Passing insights are written here as dated Markdown files

## Improving quality

The analyst prompt lives at `scripts/prompts/api_change_analyst.txt` — edit it to
tune tone, scoring, output detail level, or add domain knowledge (e.g., known breaking
change patterns for specific APIs). No code changes required.
