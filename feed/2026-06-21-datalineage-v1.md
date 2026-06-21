---
date: 2026-06-21
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Rules for BigQuery and Managed Airflow"
impact: low
breaking: false
tags: ["data-lineage", "bigquery", "airflow", "composer"]
interesting_score: 5
---

# New Ingestion Rules for BigQuery and Managed Airflow

**Date:** 2026-06-21  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API expands its ingestion rule configuration to support BigQuery and Managed Service for Apache Airflow (Cloud Composer).

## Details

Developers can now use BIGQUERY and MANAGED_AIRFLOW within the IngestionRuleIntegrationSelector to manage how lineage data is captured from these services. The LOOKER_CORE integration has also been updated and re-indexed. Additionally, the SearchLineageStreamingRequest documentation now clarifies that the locations parameter must include the location provided in the parent field, which may impact how you construct streaming search requests.

**Tags:** `data-lineage` `bigquery` `airflow` `composer`
