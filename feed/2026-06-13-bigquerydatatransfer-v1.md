---
date: 2026-06-13
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-13  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata export to Dataplex Universal Catalog, enabling automated metadata management during data transfers.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas. Developers can now specify a `metadataDestination` in `TransferConfig` and view it in `TransferRun`. This allows transfer jobs to automatically import metadata into a specified Dataplex Universal Catalog `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`), bridging the gap between data movement and data governance.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
