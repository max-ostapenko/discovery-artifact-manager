---
date: 2026-06-04
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "data-governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-04  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata export to Dataplex Universal Catalog via the new metadataDestination field.

## Details

This update introduces the ability to link data transfers with Dataplex for automated metadata management. A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes the new `DataplexConfiguration` object, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows developers to ensure that data moved via BigQuery Data Transfer is automatically discoverable and governed within the Dataplex Universal Catalog.

**Tags:** `bigquery` `dataplex` `data-governance` `metadata`
