---
date: 2026-06-17
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration for Transfers

**Date:** 2026-06-17  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports importing metadata into Dataplex Universal Catalog via a new metadata destination configuration.

## Details

The API introduces `MetadataDestination` and `DataplexConfiguration` schemas. Developers can now associate a `TransferConfig` with a Dataplex entry group by setting the `metadataDestination.dataplexConfiguration.entryGroup` field. This allows transfer metadata to be automatically cataloged in Dataplex using the format `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`. The `TransferRun` resource also now includes an output-only `metadataDestination` field to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
