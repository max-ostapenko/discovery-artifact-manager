---
date: 2026-06-19
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["pubsub", "bigtable", "compression", "data-sharing"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-19  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces a new Compression schema for message transformations, allowing ZLIB compression and decompression. Additionally, Bigtable subscription row key documentation has been updated to include message ID hashes.

## Details

The new `Compression` object allows developers to configure `compressionAlgorithm` (currently supporting `ZLIB`) and `compressionMode` (`COMPRESS` or `DECOMPRESS`) within the `MessageTransform` property. This is particularly useful for optimizing data transfer and storage costs for high-volume message streams. The `BigtableConfig` description also notes a change in the row key format, which now includes a message ID hash between the subscription name and message ID, likely to improve partition balancing in Bigtable.

**Tags:** `pubsub` `bigtable` `compression` `data-sharing`
