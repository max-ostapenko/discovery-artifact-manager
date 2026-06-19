---
date: 2026-06-19
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "data-governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Transfers

**Date:** 2026-06-19  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata export to Dataplex Universal Catalog via a new metadataDestination field.

## Details

The API introduces the `MetadataDestination` and `DataplexConfiguration` schemas. Developers can now specify a `metadataDestination` in `TransferConfig` and view it in `TransferRun`. This configuration requires an `entryGroup` string, allowing metadata from data transfers to be automatically imported into a Dataplex Universal Catalog entry group (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`).

**Tags:** `bigquery` `dataplex` `data-governance` `metadata`
