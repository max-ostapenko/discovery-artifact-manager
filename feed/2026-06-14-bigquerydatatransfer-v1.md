---
date: 2026-06-14
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-14  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Transfer configurations now support a metadata destination, enabling automatic metadata import into Dataplex Universal Catalog.

## Details

The API introduces a new `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly added `DataplexConfiguration` schema, which requires an `entryGroup` string formatted as a Dataplex Universal Catalog resource path. This allows developers to programmatically link data transfers to Dataplex for improved data discovery and governance.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
