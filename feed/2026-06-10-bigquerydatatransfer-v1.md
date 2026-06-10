---
date: 2026-06-10
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-10  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Transfer configurations now support a metadataDestination field, allowing metadata to be automatically imported into Dataplex Universal Catalog.

## Details

This update introduces the DataplexConfiguration and MetadataDestination schemas. Developers can now specify a Dataplex entry group within a TransferConfig to facilitate metadata discovery. The new metadataDestination field in TransferConfig accepts a Dataplex entry group path (projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}), and this configuration is reflected in the output of TransferRun objects.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
