---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now configure `TransferConfig` with a `metadataDestination` that points to a Dataplex `entryGroup`. This allows for automated metadata ingestion into Dataplex Universal Catalog during data transfers. The `TransferRun` resource also now includes a read-only `metadataDestination` field to track where metadata was sent for specific execution instances.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
