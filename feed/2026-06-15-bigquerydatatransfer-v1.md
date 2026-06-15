---
date: 2026-06-15
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-15  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing transfer metadata directly into Dataplex Universal Catalog.

## Details

The API introduces a new `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly added `DataplexConfiguration` schema, which requires an `entryGroup` string (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows developers to automate the registration of transferred data assets into Dataplex for better governance and discovery.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
