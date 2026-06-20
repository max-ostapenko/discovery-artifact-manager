---
date: 2026-06-20
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfer Jobs"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration for Transfer Jobs

**Date:** 2026-06-20  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the ability to route transfer metadata to Dataplex. A new schema, DataplexConfiguration, has been added to define an entryGroup (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}). This configuration is wrapped in a MetadataDestination object, which is now available as an optional field on TransferConfig for setup and as an output-only field on TransferRun for auditing.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
