---
date: 2026-06-11
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for Message Transforms"
impact: medium
breaking: false
tags: ["data-exchange", "pubsub", "compression", "bigtable"]
interesting_score: 6
---

# ZLIB compression support for Message Transforms

**Date:** 2026-06-11  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression for message data via a new MessageTransform configuration.

## Details

A new `Compression` schema has been added, allowing developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). This is integrated into the `MessageTransform` resource, enabling more efficient data handling for streaming exchanges. Additionally, the `BigtableConfig` documentation was updated to clarify that row keys now include a message ID hash for better distribution.

**Tags:** `data-exchange` `pubsub` `compression` `bigtable`
