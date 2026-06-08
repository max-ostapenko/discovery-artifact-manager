---
date: 2026-06-08
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-08  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

The API introduces the MetadataDestination and DataplexConfiguration schemas, allowing developers to link data transfers directly to Dataplex. By setting the metadataDestination field in a TransferConfig, users can specify a Dataplex entryGroup for automatic metadata importing. This configuration is also reflected in the TransferRun resource as a read-only output field to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
