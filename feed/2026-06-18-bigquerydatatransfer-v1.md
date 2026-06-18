---
date: 2026-06-18
api: bigquerydatatransfer.v1
service: BigQuery Data Transfer Service
title: "Dataplex Universal Catalog integration for transfers"
impact: medium
breaking: false
tags: ["bigquery", "dataplex", "metadata", "governance"]
interesting_score: 7
---

# Dataplex Universal Catalog integration for transfers

**Date:** 2026-06-18  
**API:** `bigquerydatatransfer.v1`  
**Impact:** Medium  

## Summary

BigQuery Data Transfer Service now supports metadata destinations, allowing transfer metadata to be automatically synced to Dataplex Universal Catalog.

## Details

The API introduces a new `metadataDestination` field to both `TransferConfig` and `TransferRun` resources. This field utilizes the newly added `MetadataDestination` and `DataplexConfiguration` schemas, enabling developers to specify a Dataplex `entryGroup` for metadata import. This integration automates the cataloging of data moved via transfer jobs into the Dataplex Universal Catalog.

**Tags:** `bigquery` `dataplex` `metadata` `governance`
