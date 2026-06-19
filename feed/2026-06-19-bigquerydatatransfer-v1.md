---
date: 2026-06-19
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-19  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex, allowing automated metadata sync with the Universal Catalog.

## Details

A new `metadataDestination` field has been added to the `TransferConfig` and `TransferRun` schemas. This field utilizes the new `DataplexConfiguration` object, which requires an `entryGroup` string (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows developers to automatically route transfer metadata into Dataplex entry groups for better data governance and discovery.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
