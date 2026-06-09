---
date: 2026-06-09
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "data-governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Transfers

**Date:** 2026-06-09  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via the new metadataDestination field.

## Details

The update introduces the DataplexConfiguration and MetadataDestination schemas. Developers can now specify an entryGroup (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}) within a TransferConfig to automatically import transfer metadata into Dataplex. This configuration is also visible in the output of TransferRun objects, allowing for better tracking of metadata lineage.

**Tags:** `bigquery` `dataplex` `data-governance` `metadata`
