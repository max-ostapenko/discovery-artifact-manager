---
date: 2026-06-16
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 6
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-16  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata exports to Dataplex, allowing developers to automatically catalog transfer metadata.

## Details

The API introduces MetadataDestination and DataplexConfiguration schemas. You can now configure TransferConfig with a metadataDestination that points to a Dataplex entryGroup (formatted as projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}). This enables the automatic import of transfer metadata into the Dataplex Universal Catalog. Correspondingly, TransferRun now includes a read-only metadataDestination field to reflect the destination used during execution.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
