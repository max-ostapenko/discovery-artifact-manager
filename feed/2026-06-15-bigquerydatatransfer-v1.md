---
date: 2026-06-15
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-15  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata directly to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the DataplexConfiguration and MetadataDestination schemas. Developers can now configure TransferConfig with a metadataDestination that points to a Dataplex entryGroup. This allows metadata from data transfers to be automatically imported into Dataplex for better data governance and discovery. The entryGroup follows the standard resource naming convention: projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
