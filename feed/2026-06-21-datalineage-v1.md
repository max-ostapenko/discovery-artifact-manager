---
date: 2026-06-21
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Sources for BigQuery and Managed Airflow"
impact: medium
breaking: false
tags: ["data-lineage", "bigquery", "airflow", "composer"]
interesting_score: 6
---

# New Ingestion Sources for BigQuery and Managed Airflow

**Date:** 2026-06-21  
**API:** `datalineage.v1`  
**Impact:** Medium  

## Summary

The Data Lineage API expanded its ingestion rule selectors to include BigQuery and Managed Airflow (Cloud Composer), while clarifying location requirements for streaming searches.

## Details

The `IngestionRuleIntegrationSelector` schema has been updated to support new integration types: `BIGQUERY` and `MANAGED_AIRFLOW`. This allows developers to more granularly control lineage ingestion from these sources. Additionally, the `SearchLineageStreamingRequest` documentation now specifies that the `locations` array must include the location provided in the `parent` field, signaling stricter validation for streaming search queries.

**Tags:** `data-lineage` `bigquery` `airflow` `composer`
