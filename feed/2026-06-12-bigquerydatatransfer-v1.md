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

Transfer configurations now support syncing metadata directly to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now specify a Dataplex `entryGroup` within a `TransferConfig` to ensure that metadata from data transfers is automatically cataloged. The `TransferRun` resource has also been updated with an output-only `metadataDestination` field to track metadata sync status for individual runs.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
