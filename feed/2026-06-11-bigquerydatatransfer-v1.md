---
date: 2026-06-11
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfers"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Transfers

**Date:** 2026-06-11  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata export to Dataplex, allowing automated metadata syncing with Dataplex Universal Catalog entry groups.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes the new `MetadataDestination` and `DataplexConfiguration` objects, enabling developers to specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) where transfer metadata should be imported. This effectively bridges data movement with automated data governance and discovery.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
