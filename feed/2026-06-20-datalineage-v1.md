---
date: 2026-06-20
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Rules for Airflow and BigQuery"
impact: medium
breaking: false
tags: ["Data Catalog", "BigQuery", "Composer", "Airflow", "Lineage"]
interesting_score: 5
---

# New Ingestion Rules for Airflow and BigQuery

**Date:** 2026-06-20  
**API:** `datalineage.v1`  
**Impact:** Medium  

## Summary

Data Lineage ingestion rules now support Managed Airflow and BigQuery integrations, alongside a clarification for streaming search locations.

## Details

The `IngestionRuleIntegrationSelector` schema has been updated to include `BIGQUERY` and `MANAGED_AIRFLOW` (Cloud Composer) as valid integration types. While existing values like `DATAPROC` and `LOOKER_CORE` were re-indexed in the discovery document, their functionality remains. Additionally, the `SearchLineageStreamingRequest` now explicitly notes that the `locations` array must contain the specific location provided in the `parent` field.

**Tags:** `Data Catalog` `BigQuery` `Composer` `Airflow` `Lineage`
