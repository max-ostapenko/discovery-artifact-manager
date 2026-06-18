---
date: 2026-06-18
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Rules for BigQuery, Looker, and Airflow"
impact: medium
breaking: false
tags: ["data-lineage", "bigquery", "looker", "airflow", "composer"]
interesting_score: 6
---

# New Ingestion Rules for BigQuery, Looker, and Airflow

**Date:** 2026-06-18  
**API:** `datalineage.v1`  
**Impact:** Medium  

## Summary

The Data Lineage API has expanded its ingestion rule selectors to support BigQuery, Looker Core, and Managed Service for Apache Airflow (Cloud Composer).

## Details

The `IngestionRuleIntegrationSelector` schema has been updated with new enum values for `BIGQUERY`, `LOOKER_CORE`, and `MANAGED_AIRFLOW`. These additions allow for more granular control over how lineage data is ingested from these specific services. Additionally, the `SearchLineageStreamingRequest` now includes a stricter requirement for the `locations` field, which must now contain the location specified in the `parent` field of the request.

**Tags:** `data-lineage` `bigquery` `looker` `airflow` `composer`
