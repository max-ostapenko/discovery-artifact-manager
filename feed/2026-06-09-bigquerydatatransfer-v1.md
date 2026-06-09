---
date: 2026-06-09
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-09  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

The BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the DataplexConfiguration and MetadataDestination schemas. Developers can now configure a TransferConfig with a metadataDestination that points to a Dataplex Universal Catalog entry group. This allows for automated metadata importing during data transfers, facilitating better data discovery and governance. The DataplexConfiguration requires an entryGroup string in the format projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
