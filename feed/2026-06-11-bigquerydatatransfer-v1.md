---
date: 2026-06-11
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-11  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadata destination configuration.

## Details

This update introduces the `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. Developers can now provide a `DataplexConfiguration` which specifies a Dataplex Universal Catalog `entryGroup` (e.g., `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows for automated metadata ingestion and governance in Dataplex as part of the data transfer lifecycle.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
