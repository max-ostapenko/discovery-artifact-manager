---
date: 2026-06-17
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-17  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports importing metadata into Dataplex Universal Catalog via a new metadata destination configuration.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes the new `MetadataDestination` and `DataplexConfiguration` objects, allowing developers to specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) for metadata ingestion during data transfers.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
