---
date: 2026-06-19
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression Support for Message Transforms"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "bigtable", "streaming"]
interesting_score: 6
---

# ZLIB Compression Support for Message Transforms

**Date:** 2026-06-19  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces a new Compression schema for message transformations, enabling ZLIB-based compression and decompression of message data.

## Details

The API now includes a `Compression` object within the `MessageTransform` schema. This allows developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (either `COMPRESS` or `DECOMPRESS`). This addition is likely aimed at optimizing payload sizes for streaming data integrations. Additionally, the documentation for `BigtableConfig` was updated to clarify that row keys are constructed using a hash of the message ID to improve data distribution.

**Tags:** `data-sharing` `compression` `bigtable` `streaming`
