---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing transfer metadata directly into Dataplex Universal Catalog.

## Details

This update introduces the `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. By configuring a `DataplexConfiguration` with a specific `entryGroup` path, developers can automate the import of metadata from their data transfers into Dataplex for better governance and discovery. The `entryGroup` must follow the format `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
