---
date: 2026-06-19
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-19  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

A new MetadataDestination object has been added to both TransferConfig and TransferRun schemas. This object contains a DataplexConfiguration which requires an entryGroup path (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}). This allows developers to automatically sync metadata from transfer operations into Dataplex for improved data governance and discovery.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
