---
date: 2026-06-09
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Data Transfers"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration for Data Transfers

**Date:** 2026-06-09  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata destinations, allowing automated metadata import into Dataplex Universal Catalog.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly introduced `MetadataDestination` and `DataplexConfiguration` schemas. Developers can now specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) to automatically catalog metadata associated with data transfers, improving data governance and discoverability.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
