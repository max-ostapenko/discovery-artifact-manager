---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["Analytics Hub", "Pub/Sub", "Bigtable", "Compression"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, enabling more efficient data movement.

## Details

A new `Compression` schema has been added to the API, allowing developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (either `COMPRESS` or `DECOMPRESS`). This configuration is now available as an optional `compression` field within the `MessageTransform` resource. Additionally, the `BigtableConfig` documentation was updated to clarify that row keys are constructed using a message ID hash to ensure better data distribution.

**Tags:** `Analytics Hub` `Pub/Sub` `Bigtable` `Compression`
