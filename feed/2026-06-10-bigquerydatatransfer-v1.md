---
date: 2026-06-10
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-10  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

This update introduces the `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. Developers can now configure transfers to automatically import metadata into a Dataplex Universal Catalog entry group by providing a `DataplexConfiguration` object. The configuration requires an `entryGroup` path in the format `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
