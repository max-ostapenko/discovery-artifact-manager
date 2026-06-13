---
date: 2026-06-13
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-13  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata destinations, allowing automated metadata import into Dataplex Universal Catalog.

## Details

The API introduces a new `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly added `DataplexConfiguration` schema, which requires an `entryGroup` string (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This enables developers to automatically sync metadata from their data transfers directly into Dataplex for better governance and discovery.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
