---
date: 2026-06-11
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Catalog support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex Catalog support

**Date:** 2026-06-11  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Transfer configurations can now automatically sync metadata into the Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the DataplexConfiguration and MetadataDestination schemas. Developers can now configure TransferConfig with a metadataDestination that points to a specific Dataplex entryGroup (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}). Additionally, TransferRun now includes an output-only metadataDestination field to track metadata import status for specific executions.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
