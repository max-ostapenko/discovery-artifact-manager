---
date: 2026-06-19
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Rules for Looker and Managed Airflow"
impact: low
breaking: false
tags: ["data-lineage", "looker", "airflow", "composer", "bigquery"]
interesting_score: 5
---

# New Ingestion Rules for Looker and Managed Airflow

**Date:** 2026-06-19  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API now supports ingestion rules for Looker Core and Managed Service for Apache Airflow (Cloud Composer), alongside BigQuery.

## Details

The `IngestionRuleIntegrationSelector` schema has been expanded to include `LOOKER_CORE` and `MANAGED_AIRFLOW` as valid integration types. Additionally, `BIGQUERY` has been explicitly added to the integration enum. The documentation for `SearchLineageStreamingRequest` was also updated to clarify that the `locations` list must contain the location specified in the `parent` field.

**Tags:** `data-lineage` `looker` `airflow` `composer` `bigquery`
