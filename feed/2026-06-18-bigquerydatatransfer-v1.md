---
date: 2026-06-18
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for metadata"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for metadata

**Date:** 2026-06-18  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now specify a `metadataDestination` within a `TransferConfig` to automatically import transfer metadata into a Dataplex `entryGroup`. The `entryGroup` field requires a specific resource path format: `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`. Additionally, `TransferRun` objects now include this destination in their output for auditability.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
