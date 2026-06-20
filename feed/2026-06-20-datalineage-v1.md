---
date: 2026-06-20
api: datalineage.v1
service: Data Lineage
title: "New Ingestion Sources for BigQuery and Airflow"
impact: medium
breaking: false
tags: ["data-lineage", "bigquery", "airflow", "composer"]
interesting_score: 6
---

# New Ingestion Sources for BigQuery and Airflow

**Date:** 2026-06-20  
**API:** `datalineage.v1`  
**Impact:** Medium  

## Summary

The Data Lineage API expands its ingestion rule selectors to include BigQuery, Looker Core, and Managed Service for Apache Airflow.

## Details

Developers can now configure ingestion rules using the IngestionRuleIntegrationSelector with new enum values: BIGQUERY, LOOKER_CORE, and MANAGED_AIRFLOW (Cloud Composer). Additionally, the SearchLineageStreamingRequest has a clarified requirement: the locations parameter must now explicitly contain the location provided in the parent field.

**Tags:** `data-lineage` `bigquery` `airflow` `composer`
