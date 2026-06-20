---
date: 2026-06-20
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-20  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

The API introduces a `metadataDestination` field to both `TransferConfig` and `TransferRun` schemas. This field utilizes a new `DataplexConfiguration` object, allowing developers to specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) where transfer metadata should be imported. This effectively bridges the gap between automated data movement and centralized metadata governance.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
