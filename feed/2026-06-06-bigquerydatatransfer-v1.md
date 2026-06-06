---
date: 2026-06-06
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-06  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata synchronization with Dataplex, allowing automated metadata import into the Universal Catalog.

## Details

The API introduces a new `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly added `DataplexConfiguration` schema, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows developers to automatically route metadata from data transfers into specific Dataplex entry groups for better data governance and discoverability.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
