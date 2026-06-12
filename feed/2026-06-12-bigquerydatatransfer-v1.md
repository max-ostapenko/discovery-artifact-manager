---
date: 2026-06-12
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-12  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Developers can now configure data transfers to automatically sync metadata to Dataplex Universal Catalog via the new metadataDestination field.

## Details

This update introduces the DataplexConfiguration and MetadataDestination schemas to the TransferConfig resource. By setting the metadataDestination.dataplexConfiguration.entryGroup field, users can specify a Dataplex Universal Catalog entry group (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}) where transfer metadata should be imported. The TransferRun resource also gains a read-only metadataDestination field to track metadata sync status for specific executions.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
