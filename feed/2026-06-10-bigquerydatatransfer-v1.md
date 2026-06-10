---
date: 2026-06-10
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for Data Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for Data Transfers

**Date:** 2026-06-10  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

The API introduces a `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the new `DataplexConfiguration` schema, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows developers to automatically register and manage metadata in Dataplex as part of their data transfer workflows.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
