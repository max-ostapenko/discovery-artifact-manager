---
date: 2026-06-08
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-08  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now configure `TransferConfig` objects with a `metadataDestination` that points to a Dataplex `entryGroup`. This allows for automated metadata ingestion into Dataplex's governance layer during data transfers. The `TransferRun` resource has also been updated to include this destination as a read-only field for auditing purposes.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
