---
date: 2026-06-12
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-12  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata synchronization with Dataplex, allowing transfer metadata to be automatically imported into the Universal Catalog.

## Details

This update introduces the `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes a new `DataplexConfiguration` schema, which requires an `entryGroup` string (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows developers to link data transfers directly to Dataplex governance and discovery workflows.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
