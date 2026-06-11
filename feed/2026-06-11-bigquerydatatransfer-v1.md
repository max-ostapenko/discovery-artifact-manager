---
date: 2026-06-11
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "data-governance", "metadata"]
interesting_score: 7
---

# BigQuery Data Transfer adds Dataplex metadata support

**Date:** 2026-06-11  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

The API introduces the `MetadataDestination` and `DataplexConfiguration` schemas, allowing transfers to automatically import metadata into Dataplex. Developers can now set the `metadataDestination` field on a `TransferConfig` by providing a Dataplex `entryGroup` path. Correspondingly, `TransferRun` objects now include an output-only `metadataDestination` field to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `data-governance` `metadata`
