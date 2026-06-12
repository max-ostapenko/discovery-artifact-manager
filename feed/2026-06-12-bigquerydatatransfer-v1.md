---
date: 2026-06-12
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-12  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

The API introduces 'MetadataDestination' and 'DataplexConfiguration' schemas, allowing transfer configurations to sync metadata with Dataplex. Developers can now specify an 'entryGroup' within 'TransferConfig.metadataDestination' to automatically import transfer metadata into the Dataplex Universal Catalog. This change also adds a read-only 'metadataDestination' field to 'TransferRun' to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
