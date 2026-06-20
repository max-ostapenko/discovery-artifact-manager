---
date: 2026-06-20
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Rules for Looker and Managed Airflow"
impact: medium
breaking: false
tags: ["data-lineage", "looker", "airflow", "bigquery"]
interesting_score: 5
---

# New Ingestion Rules for Looker and Managed Airflow

**Date:** 2026-06-20  
**API:** `datalineage.v1`  
**Impact:** Medium  

## Summary

The Data Lineage API expands its ingestion rule selectors to support Looker Core and Managed Service for Apache Airflow, while clarifying location requirements for streaming searches.

## Details

The `IngestionRuleIntegrationSelector` schema has been updated to include `LOOKER_CORE` and `MANAGED_AIRFLOW` (Cloud Composer) as valid integration types. The enum list was also reorganized to explicitly include `BIGQUERY`. Additionally, the `SearchLineageStreamingRequest` now includes a documentation clarification that the `locations` list must contain the specific location provided in the `parent` field.

**Tags:** `data-lineage` `looker` `airflow` `bigquery`
