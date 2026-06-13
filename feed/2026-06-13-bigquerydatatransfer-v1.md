---
date: 2026-06-13
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-13  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata synchronization with Dataplex Universal Catalog.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` resources. This allows developers to specify a `DataplexConfiguration` containing an `entryGroup`, enabling automatic metadata import into Dataplex during data transfer operations. The `entryGroup` must follow the format `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
