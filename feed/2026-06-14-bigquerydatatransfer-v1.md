---
date: 2026-06-14
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "data-governance"]
interesting_score: 6
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-14  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Transfer configurations now support a metadata destination, allowing automatic metadata import into Dataplex Universal Catalog.

## Details

This update introduces the `MetadataDestination` and `DataplexConfiguration` schemas to the API. Developers can now set the `metadataDestination` field on a `TransferConfig` to point to a specific Dataplex `entryGroup`. This enables the automatic cataloging of transferred data metadata. The `TransferRun` resource has also been updated to include this destination as an output-only field, providing traceability for where metadata was synced during a specific run.

**Tags:** `bigquery` `dataplex` `metadata` `data-governance`
