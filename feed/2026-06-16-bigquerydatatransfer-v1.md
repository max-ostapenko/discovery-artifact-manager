---
date: 2026-06-16
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-16  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports importing metadata directly into Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now configure `TransferConfig` with a `metadataDestination` that points to a Dataplex `entryGroup`. This allows for automated metadata synchronization between BigQuery transfers and Dataplex governance tools. The `TransferRun` resource also now includes an output-only `metadataDestination` field to track where metadata was sent during a specific execution.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
