---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas, allowing transfers to sync metadata into Dataplex. A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` resources. To use this, developers must provide an `entryGroup` in the format `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}` within the `DataplexConfiguration` object.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
