---
date: 2026-06-15
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-15  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports automated metadata export to Dataplex Universal Catalog via new configuration fields.

## Details

The API introduces a `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field points to a new `DataplexConfiguration` schema, which allows developers to specify a Dataplex Universal Catalog `entryGroup`. This enables automatic metadata ingestion into Dataplex when data transfers occur, bridging the gap between data movement and data governance.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
