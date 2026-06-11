---
date: 2026-06-11
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Data Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Data Transfers

**Date:** 2026-06-11  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata destinations, allowing users to automatically sync transfer metadata to Dataplex Universal Catalog.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes the new `DataplexConfiguration` object, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This integration enables the automatic import of metadata into the Dataplex Universal Catalog during data transfer operations, facilitating better data discovery and governance.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
