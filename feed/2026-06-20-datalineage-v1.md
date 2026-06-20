---
date: 2026-06-20
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Rule Integrations for BigQuery and Airflow"
impact: medium
breaking: false
tags: ["Data Lineage", "BigQuery", "Airflow", "Cloud Composer"]
interesting_score: 5
---

# New Ingestion Rule Integrations for BigQuery and Airflow

**Date:** 2026-06-20  
**API:** `datalineage.v1`  
**Impact:** Medium  

## Summary

The Data Lineage API now supports BigQuery and Managed Service for Apache Airflow (Cloud Composer) in ingestion rules.

## Details

The IngestionRuleIntegrationSelector schema has been expanded to include BIGQUERY and MANAGED_AIRFLOW (Cloud Composer) as valid integration types. This allows developers to configure specific ingestion rules for these services. Additionally, the SearchLineageStreamingRequest now includes a documentation clarification that the 'locations' field must contain the location specified in the 'parent' field.

**Tags:** `Data Lineage` `BigQuery` `Airflow` `Cloud Composer`
