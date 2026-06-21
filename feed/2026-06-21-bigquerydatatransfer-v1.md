---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 6
---

# Dataplex Universal Catalog Integration for Transfers

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the ability to route transfer metadata to Dataplex. A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes a `DataplexConfiguration` object where developers must specify an `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows for automated metadata ingestion and governance within the Dataplex Universal Catalog as data moves through the transfer service.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
