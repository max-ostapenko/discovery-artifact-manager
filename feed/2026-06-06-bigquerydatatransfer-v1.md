---
date: 2026-06-06
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex metadata integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 6
---

# BigQuery Data Transfer adds Dataplex metadata integration

**Date:** 2026-06-06  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

The API introduces `MetadataDestination` and `DataplexConfiguration` schemas. Both `TransferConfig` and `TransferRun` have been updated to include a `metadataDestination` field. This allows developers to specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) where transfer metadata will be automatically imported, facilitating better data governance and discovery.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
