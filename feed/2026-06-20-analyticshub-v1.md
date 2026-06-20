---
date: 2026-06-20
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-transfer", "compression", "pubsub", "bigtable"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-20  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, enabling more efficient data movement.

## Details

A new `Compression` schema has been added to the API, allowing developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). This configuration is now available via the `compression` field on the `MessageTransform` resource. Additionally, the `BigtableConfig` documentation was updated to reflect that row keys now include a message ID hash for better distribution.

**Tags:** `data-transfer` `compression` `pubsub` `bigtable`
