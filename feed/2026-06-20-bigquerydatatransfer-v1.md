---
date: 2026-06-20
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-20  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata export to Dataplex, allowing automated metadata syncing during data transfers.

## Details

The API introduces a new `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the new `MetadataDestination` and `DataplexConfiguration` schemas, enabling developers to specify a Dataplex Universal Catalog entry group (via the `entryGroup` parameter) as a destination for transfer metadata. The entry group must follow the standard resource name format: `projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}`.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
