---
date: 2026-06-14
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression Support for Message Transformations"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "bigtable", "pubsub"]
interesting_score: 6
---

# ZLIB Compression Support for Message Transformations

**Date:** 2026-06-14  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression for message data via a new MessageTransform schema.

## Details

The API introduces a `Compression` schema that allows developers to specify a `compressionAlgorithm` (ZLIB) and a `compressionMode` (COMPRESS or DECOMPRESS). This is integrated into the `MessageTransform` resource, enabling more efficient data handling for streaming subscriptions. Additionally, the documentation for `BigtableConfig` was updated to reflect that row keys now include a message ID hash, which is a critical detail for Bigtable performance and hotspot avoidance.

**Tags:** `data-sharing` `compression` `bigtable` `pubsub`
