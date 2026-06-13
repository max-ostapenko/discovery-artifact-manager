---
date: 2026-06-13
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-13  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata directly to Dataplex Universal Catalog via a new metadataDestination configuration.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas. Developers can now specify a `metadataDestination` in `TransferConfig` to automatically import transfer metadata into a specific Dataplex `entryGroup`. The `TransferRun` resource also includes this field as output-only to track where metadata was sent during a specific execution.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
