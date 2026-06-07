---
date: 2026-06-07
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for Data Transfers"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for Data Transfers

**Date:** 2026-06-07  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata synchronization with Dataplex, allowing transfer metadata to be automatically imported into the Universal Catalog.

## Details

A new `metadataDestination` field has been added to the `TransferConfig` and `TransferRun` schemas. This field allows developers to specify a `DataplexConfiguration` containing an `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This integration enables better data governance by ensuring that metadata from data transfers is searchable and manageable within Dataplex.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
