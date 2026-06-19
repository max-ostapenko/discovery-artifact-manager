---
date: 2026-06-19
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Rules for BigQuery and Managed Airflow"
impact: medium
breaking: false
tags: ["Data Lineage", "BigQuery", "Cloud Composer", "Airflow"]
interesting_score: 5
---

# New Ingestion Rules for BigQuery and Managed Airflow

**Date:** 2026-06-19  
**API:** `datalineage.v1`  
**Impact:** Medium  

## Summary

Data Lineage adds support for BigQuery and Managed Airflow (Cloud Composer) ingestion rules, alongside clarified location requirements for streaming searches.

## Details

The IngestionRuleIntegrationSelector schema has been updated with new integration types: BIGQUERY, LOOKER_CORE, and MANAGED_AIRFLOW. This allows for more granular control over how lineage data is ingested from these services. Furthermore, the SearchLineageStreamingRequest now explicitly requires that the locations array contains the location provided in the parent field, which may affect how developers construct streaming search queries.

**Tags:** `Data Lineage` `BigQuery` `Cloud Composer` `Airflow`
