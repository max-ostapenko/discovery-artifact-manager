---
date: 2026-06-04
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-04  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports automated metadata synchronization with Dataplex Universal Catalog.

## Details

The API introduces a new `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly added `MetadataDestination` and `DataplexConfiguration` schemas, allowing developers to specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) as a target for metadata generated during data transfers.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
