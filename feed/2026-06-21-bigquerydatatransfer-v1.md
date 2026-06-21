---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the ability to route transfer metadata to Dataplex. A new `MetadataDestination` object has been added to both `TransferConfig` and `TransferRun` schemas. This object contains a `DataplexConfiguration` which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows for automated metadata ingestion into Dataplex's governance layer as part of the standard data transfer workflow.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
