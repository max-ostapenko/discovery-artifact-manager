---
date: 2026-06-21
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for Data Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for Data Transfers

**Date:** 2026-06-21  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports exporting metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` resources. This field utilizes the `DataplexConfiguration` schema, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This allows developers to automate the registration of transferred data's metadata into Dataplex for better cataloging and governance.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
