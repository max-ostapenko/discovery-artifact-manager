---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata export to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the ability to link data transfers directly to Dataplex for metadata management. A new `MetadataDestination` object has been added to the `TransferConfig` and `TransferRun` schemas. This object contains a `DataplexConfiguration` which requires an `entryGroup` path. This allows developers to automatically catalog transfer metadata into specific Dataplex entry groups, facilitating better data governance and discovery.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
