---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["Analytics Hub", "Pub/Sub", "Compression", "Data Engineering"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, allowing for more efficient data handling.

## Details

A new `Compression` schema has been introduced and integrated into `MessageTransform`. This allows developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). Additionally, the documentation for `BigtableConfig` was updated to reflect that row keys now include a message ID hash, which improves data distribution in Bigtable-backed subscriptions.

**Tags:** `Analytics Hub` `Pub/Sub` `Compression` `Data Engineering`
