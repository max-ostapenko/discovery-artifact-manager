---
date: 2026-06-15
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog Integration for Data Transfers"
impact: medium
breaking: false
tags: ["BigQuery", "Dataplex", "Data Governance", "Metadata"]
interesting_score: 7
---

# Dataplex Universal Catalog Integration for Data Transfers

**Date:** 2026-06-15  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata destinations, allowing transfer metadata to be automatically imported into Dataplex Universal Catalog.

## Details

A new `metadataDestination` field has been added to both `TransferConfig` and `TransferRun` resources. This field accepts a `DataplexConfiguration` object, which requires an `entryGroup` string formatted as a Dataplex resource path. This allows developers to automate the registration of transferred data metadata into the Dataplex Universal Catalog for improved data governance and discovery.

**Tags:** `BigQuery` `Dataplex` `Data Governance` `Metadata`
