---
date: 2026-06-20
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-20  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the ability to link data transfers with Dataplex for better metadata management. A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes the new `DataplexConfiguration` object, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows developers to automatically catalog transfer metadata into Dataplex entry groups as part of the transfer process.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
