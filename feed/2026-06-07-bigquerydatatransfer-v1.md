---
date: 2026-06-07
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "BigQuery Data Transfer adds Dataplex Metadata support"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 6
---

# BigQuery Data Transfer adds Dataplex Metadata support

**Date:** 2026-06-07  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

Transfer configurations now support a metadataDestination field, enabling automatic metadata import into Dataplex Universal Catalog.

## Details

The API introduces DataplexConfiguration and MetadataDestination schemas. Developers can now specify a metadataDestination within TransferConfig and TransferRun resources. This allows for the automatic synchronization of transfer metadata into a Dataplex Universal Catalog entry group, specified by the entryGroup string parameter (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}).

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
