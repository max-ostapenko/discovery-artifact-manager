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

The Data Lineage API now supports ingestion rules for Looker Core and Managed Service for Apache Airflow (Cloud Composer), alongside BigQuery.

## Details

The `IngestionRuleIntegrationSelector` schema has been expanded to include new enum values for `LOOKER_CORE`, `MANAGED_AIRFLOW`, and `BIGQUERY`. This allows for more granular control over lineage ingestion from these specific services. Additionally, the `SearchLineageStreamingRequest` documentation now explicitly requires that the `locations` list includes the location specified in the `parent` field of the request.

**Tags:** `data-lineage` `looker` `airflow` `bigquery`
