---
date: 2026-06-08
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for Data Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for Data Transfers

**Date:** 2026-06-08  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata directly to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now set the `metadataDestination` field on a `TransferConfig` to point to a specific Dataplex `entryGroup`. This allows for automated metadata ingestion into Dataplex as part of the transfer process. Correspondingly, `TransferRun` objects now include an output-only `metadataDestination` field to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
