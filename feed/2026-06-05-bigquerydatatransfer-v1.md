---
date: 2026-06-05
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata Sync"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "data-governance", "metadata"]
interesting_score: 6
---

# BigQuery Data Transfer adds Dataplex Metadata Sync

**Date:** 2026-06-05  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the DataplexConfiguration and MetadataDestination schemas, allowing developers to link data transfers to Dataplex. By setting the metadataDestination field in a TransferConfig, you can now automatically import transfer metadata into a specific Dataplex entryGroup. The TransferRun resource also gains a read-only metadataDestination field to track metadata routing for individual execution instances.

**Tags:** `bigquery` `dataplex` `data-governance` `metadata`
