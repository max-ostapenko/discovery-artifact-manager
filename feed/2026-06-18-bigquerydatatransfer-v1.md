---
date: 2026-06-18
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Transfers

**Date:** 2026-06-18  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata destinations, allowing transfer metadata to be automatically imported into Dataplex Universal Catalog.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` schemas. This field utilizes the new `DataplexConfiguration` object, which requires an `entryGroup` path (formatted as `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`). This enables seamless metadata synchronization between BigQuery transfers and Dataplex's cataloging features, improving data discoverability and governance.

**Tags:** `bigquery` `dataplex` `governance` `metadata`
