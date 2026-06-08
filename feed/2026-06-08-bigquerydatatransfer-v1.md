---
date: 2026-06-08
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Metadata", "Data Governance"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-08  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing transfer metadata directly into the Dataplex Universal Catalog.

## Details

The API introduces a new `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly added `MetadataDestination` and `DataplexConfiguration` schemas, allowing developers to specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) where metadata from data transfers will be automatically imported for better data governance and discovery.

**Tags:** `BigQuery` `Dataplex` `Metadata` `Data Governance`
