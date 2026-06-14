---
date: 2026-06-14
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "data-governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Transfers

**Date:** 2026-06-14  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via the new metadataDestination field.

## Details

The update introduces DataplexConfiguration and MetadataDestination schemas. Developers can now configure a TransferConfig with a metadataDestination that points to a Dataplex entryGroup (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}). This enables automated metadata management for data transfers. The TransferRun resource also includes this destination as an output-only field to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `data-governance` `metadata`
