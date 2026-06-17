---
date: 2026-06-17
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-pipelines", "pubsub", "compression", "bigtable"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-17  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, enabling more efficient data movement.

## Details

A new `Compression` schema has been added to the API, allowing developers to configure `ZLIB` compression or decompression via the `MessageTransform` resource. This includes a `compressionAlgorithm` field and a `compressionMode` field (COMPRESS/DECOMPRESS). Additionally, the `BigtableConfig` documentation was updated to reflect that row keys now include a message ID hash for better distribution.

**Tags:** `data-pipelines` `pubsub` `compression` `bigtable`
