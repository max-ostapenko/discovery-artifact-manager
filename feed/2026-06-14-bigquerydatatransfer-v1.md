---
date: 2026-06-14
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-14  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Transfer configurations can now automatically sync metadata to the Dataplex Universal Catalog.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the BigQuery Data Transfer API. Developers can now specify a `metadataDestination` within `TransferConfig` and `TransferRun` objects, allowing transfer metadata to be imported directly into a Dataplex `entryGroup`. The configuration requires a specific resource path format: `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
