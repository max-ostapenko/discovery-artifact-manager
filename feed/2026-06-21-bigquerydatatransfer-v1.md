---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Developers can now configure transfer jobs to automatically sync metadata to Dataplex Universal Catalog via the new metadataDestination field.

## Details

The update introduces the MetadataDestination and DataplexConfiguration schemas to the TransferConfig and TransferRun resources. When configuring a transfer, you can now specify a Dataplex entry group (formatted as projects/{project}/locations/{region}/entryGroups/{id}) to automatically import metadata. This allows for better integration between BigQuery data movement and centralized data governance in Dataplex.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
