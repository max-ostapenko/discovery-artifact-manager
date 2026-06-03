---
date: 2026-06-03
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-03  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog.

## Details

This update introduces the ability to link data transfers with Dataplex for better metadata governance. A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes the newly added `DataplexConfiguration` object, which requires an `entryGroup` path in the format `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
