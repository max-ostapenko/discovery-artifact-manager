---
date: 2026-06-16
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for Data Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for Data Transfers

**Date:** 2026-06-16  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata synchronization with Dataplex Universal Catalog via new configuration fields.

## Details

The API introduces the `MetadataDestination` and `DataplexConfiguration` schemas. Developers can now specify a `metadataDestination` within `TransferConfig` and `TransferRun` objects. This allows transferred data metadata to be automatically imported into a Dataplex Universal Catalog `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`), facilitating better data discovery and governance.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
