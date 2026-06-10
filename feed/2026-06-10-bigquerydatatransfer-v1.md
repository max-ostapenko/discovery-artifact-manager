---
date: 2026-06-10
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-10  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

The API introduces the `MetadataDestination` and `DataplexConfiguration` schemas. Developers can now configure `TransferConfig` with a `metadataDestination` that points to a specific Dataplex `entryGroup`. This allows for the automatic import of transfer metadata into the Dataplex Universal Catalog. Correspondingly, `TransferRun` now includes an output-only `metadataDestination` field to track metadata delivery for specific runs.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
