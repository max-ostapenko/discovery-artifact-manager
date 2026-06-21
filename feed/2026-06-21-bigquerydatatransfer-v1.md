---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now configure `TransferConfig` with a `metadataDestination` that points to a Dataplex `entryGroup`. This allows for the automatic import of metadata into the Dataplex Universal Catalog during transfer operations. The `TransferRun` resource also includes this field as an output-only property to track metadata sync status for specific runs.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
