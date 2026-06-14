---
date: 2026-06-14
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-14  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the ability to route transfer metadata to Dataplex. A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes the `DataplexConfiguration` object, which requires an `entryGroup` string formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`. This allows developers to automate the cataloging of transferred data within the Dataplex Universal Catalog ecosystem.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
