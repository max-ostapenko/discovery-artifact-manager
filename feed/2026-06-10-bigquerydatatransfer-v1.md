---
date: 2026-06-10
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Transfers

**Date:** 2026-06-10  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata destinations, allowing transfer metadata to be automatically imported into Dataplex Universal Catalog.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now configure a `metadataDestination` on a `TransferConfig` by specifying a Dataplex `entryGroup`. This allows for automated metadata management where transfer details are synced to a specific Dataplex Universal Catalog entry group (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). The `TransferRun` resource also gains a read-only `metadataDestination` field to track where metadata was sent during execution.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
