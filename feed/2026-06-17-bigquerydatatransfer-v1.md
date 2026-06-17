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

BigQuery Data Transfer Service now supports metadata destinations, allowing automated metadata import into Dataplex Universal Catalog.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly introduced `DataplexConfiguration` schema, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This enables developers to automatically sync transfer metadata into Dataplex for better data governance and discoverability.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
