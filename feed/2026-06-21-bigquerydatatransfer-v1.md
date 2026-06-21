---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via the new MetadataDestination field.

## Details

This update introduces the 'MetadataDestination' and 'DataplexConfiguration' schemas to the TransferConfig and TransferRun resources. Developers can now configure transfers to automatically import metadata into a Dataplex Universal Catalog entry group by specifying the 'entryGroup' path (formatted as 'projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}'). This allows for better data governance and discovery of transferred datasets within the Dataplex ecosystem.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
