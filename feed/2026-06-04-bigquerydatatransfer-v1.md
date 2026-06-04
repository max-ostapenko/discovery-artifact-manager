---
date: 2026-06-04
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-04  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata export to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the ability to sync transfer metadata into Dataplex. A new `metadataDestination` field has been added to the `TransferConfig` and `TransferRun` schemas. This field utilizes the newly added `DataplexConfiguration` object, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) to specify where the Universal Catalog metadata should be imported.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
