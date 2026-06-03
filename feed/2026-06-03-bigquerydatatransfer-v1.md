---
date: 2026-06-03
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-03  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports importing metadata into Dataplex Universal Catalog via a new metadata destination configuration.

## Details

The API has introduced a `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the new `DataplexConfiguration` schema, allowing developers to specify a Dataplex Universal Catalog `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) where transfer metadata should be imported. This effectively bridges data movement with centralized data governance and discovery.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
