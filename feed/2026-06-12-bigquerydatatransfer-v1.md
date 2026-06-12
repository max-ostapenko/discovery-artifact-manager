---
date: 2026-06-12
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration

**Date:** 2026-06-12  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports importing metadata into Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the MetadataDestination and DataplexConfiguration schemas. Developers can now configure TransferConfig with a metadataDestination, allowing transfer metadata to be automatically synced to a Dataplex entryGroup (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}). The TransferRun resource has also been updated to include this destination as an output-only field for tracking purposes.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
