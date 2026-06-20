---
date: 2026-06-20
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-20  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via new configuration fields.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now specify a `metadataDestination` in `TransferConfig` and `TransferRun` objects. This allows for the automatic import of transfer metadata into a specific Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`), facilitating better data governance and discovery within the Dataplex Universal Catalog.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
