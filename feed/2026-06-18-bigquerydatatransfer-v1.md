---
date: 2026-06-18
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-transfer"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-18  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Transfer configurations now support a `metadataDestination` field, allowing automatic metadata import into Dataplex Universal Catalog.

## Details

The API introduces `DataplexConfiguration` and `MetadataDestination` schemas. Developers can now specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) within `TransferConfig.metadataDestination` to sync metadata during transfers. The `TransferRun` resource also includes this field as output to track metadata destination status.

**Tags:** `bigquery` `dataplex` `metadata` `data-transfer`
