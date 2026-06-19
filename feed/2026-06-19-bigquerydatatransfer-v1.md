---
date: 2026-06-19
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-19  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas. Developers can now specify a Dataplex `entryGroup` within a `TransferConfig` to automatically import transfer metadata into the Dataplex Universal Catalog. The `TransferRun` resource also includes this destination as an output-only field to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
