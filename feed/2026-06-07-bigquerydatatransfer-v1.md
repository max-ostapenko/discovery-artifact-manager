---
date: 2026-06-07
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Data Transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "governance", "metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Data Transfers

**Date:** 2026-06-07  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports syncing metadata to Dataplex Universal Catalog for improved data governance.

## Details

This update introduces the ability to specify a metadata destination for transfer configurations. A new `MetadataDestination` schema has been added, which includes a `DataplexConfiguration`. This allows developers to link transfers to a Dataplex Universal Catalog `entryGroup`. These fields have been added to both the `TransferConfig` (for setup) and the `TransferRun` (as output-only metadata).

**Tags:** `bigquery` `dataplex` `governance` `metadata`
