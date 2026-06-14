---
date: 2026-06-14
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "bigtable"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-14  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces a new Compression schema for message transformations, allowing developers to specify ZLIB compression or decompression for data streams.

## Details

A new `Compression` object has been added to the `MessageTransform` schema. This allows for configuring `compressionAlgorithm` (currently supporting `ZLIB`) and `compressionMode` (`COMPRESS` or `DECOMPRESS`). Additionally, documentation for `BigtableConfig` was updated to clarify that row keys now include a message ID hash, which is a standard practice for preventing hotspots in Bigtable.

**Tags:** `data-sharing` `compression` `bigtable`
