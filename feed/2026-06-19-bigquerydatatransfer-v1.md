---
date: 2026-06-19
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "data-governance", "metadata"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-19  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

A new MetadataDestination object has been added to both TransferConfig and TransferRun schemas. This object contains a DataplexConfiguration which requires an entryGroup path (e.g., projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}). This allows developers to automatically sync transfer metadata into Dataplex for better data governance and discovery.

**Tags:** `bigquery` `dataplex` `data-governance` `metadata`
