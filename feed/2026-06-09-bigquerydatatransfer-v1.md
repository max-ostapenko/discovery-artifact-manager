---
date: 2026-06-09
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-09  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via new configuration fields.

## Details

This update introduces the ability to sync transfer metadata into Dataplex. A new `metadataDestination` field has been added to the `TransferConfig` and `TransferRun` schemas. This field utilizes the newly defined `MetadataDestination` and `DataplexConfiguration` objects, allowing developers to specify a Dataplex `entryGroup` (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`) as a target for metadata import.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
