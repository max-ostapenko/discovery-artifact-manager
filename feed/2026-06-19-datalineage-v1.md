---
date: 2026-06-19
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Rule Integrations for Looker and Airflow"
impact: medium
breaking: false
tags: ["data-lineage", "looker", "airflow", "bigquery"]
interesting_score: 5
---

# New Ingestion Rule Integrations for Looker and Airflow

**Date:** 2026-06-19  
**API:** `datalineage.v1`  
**Impact:** Medium  

## Summary

The Data Lineage API expanded its ingestion rule selectors to support Looker Core, BigQuery, and Managed Service for Apache Airflow (Cloud Composer).

## Details

The `IngestionRuleIntegrationSelector` schema has been updated to include `LOOKER_CORE`, `MANAGED_AIRFLOW`, and `BIGQUERY` as valid integration types. This allows for more granular control over how lineage data is ingested from these specific services. Additionally, the `SearchLineageStreamingRequest` now explicitly requires that the `locations` list includes the location specified in the `parent` field, clarifying a previously ambiguous requirement for streaming searches.

**Tags:** `data-lineage` `looker` `airflow` `bigquery`
