---
date: 2026-06-15
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-ingestion", "compression", "bigtable"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-15  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, enabling more efficient data transfer.

## Details

A new `Compression` schema has been added to the API, allowing developers to specify `compressionAlgorithm` (currently supporting `ZLIB`) and `compressionMode` (COMPRESS or DECOMPRESS). This is integrated into the `MessageTransform` resource. Additionally, the `BigtableConfig` documentation was updated to reflect a change in how row keys are constructed, now including a message ID hash for improved data distribution.

**Tags:** `data-ingestion` `compression` `bigtable`
