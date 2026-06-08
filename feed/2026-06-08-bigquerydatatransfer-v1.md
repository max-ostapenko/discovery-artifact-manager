---
date: 2026-06-08
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Catalog support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex Catalog support

**Date:** 2026-06-08  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

The BigQuery Data Transfer Service now supports metadata synchronization with Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the ability to link data transfers directly to Dataplex. New schemas `DataplexConfiguration` and `MetadataDestination` have been added. Developers can now set the `metadataDestination` property on a `TransferConfig` to specify a Dataplex `entryGroup`. This allows for automatic metadata ingestion into the Dataplex Universal Catalog, facilitating better data discovery and governance. The `TransferRun` resource also now includes this field as an output-only property to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
