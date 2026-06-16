---
date: 2026-06-16
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-16  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports importing transfer metadata into Dataplex Universal Catalog via a new metadata destination configuration.

## Details

The API introduces a `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the new `DataplexConfiguration` schema, which requires an `entryGroup` identifier. This allows developers to automatically sync metadata from data transfers into specific Dataplex entry groups for better data governance and discovery.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
