---
date: 2026-06-17
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-17  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to `TransferConfig` and `TransferRun`. Developers can now specify an `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) to automatically import transfer metadata into Dataplex. The `metadataDestination` field in `TransferRun` is output-only, allowing for auditability of where metadata was dispatched during a specific run.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
