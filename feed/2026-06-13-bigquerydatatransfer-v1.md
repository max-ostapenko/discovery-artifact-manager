---
date: 2026-06-13
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-13  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via the new MetadataDestination field.

## Details

This update introduces the ability to route transfer metadata to Dataplex. A new schema `DataplexConfiguration` has been added, requiring an `entryGroup` string. Both `TransferConfig` and `TransferRun` resources now include a `metadataDestination` field. This allows developers to automate the registration of transferred data into Dataplex's governance layer by specifying a target entry group in the format `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
