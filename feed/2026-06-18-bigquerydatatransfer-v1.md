---
date: 2026-06-18
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Automated Dataplex Metadata Sync for Data Transfers"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Metadata", "Data Governance"]
interesting_score: 6
---

# Automated Dataplex Metadata Sync for Data Transfers

**Date:** 2026-06-18  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog via a new metadataDestination field.

## Details

This update introduces the MetadataDestination and DataplexConfiguration objects to the TransferConfig and TransferRun resources. Developers can now provide a Dataplex entryGroup ID to automatically import transfer metadata into the Universal Catalog. The entryGroup must follow the standard GCP resource path format: projects/{project_id}/locations/{region}/entryGroups/{entry_group_id}.

**Tags:** `BigQuery` `Dataplex` `Metadata` `Data Governance`
