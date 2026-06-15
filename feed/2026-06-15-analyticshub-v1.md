---
date: 2026-06-15
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["data-transfer", "compression", "bigtable", "pubsub"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-15  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside updated row key logic for Bigtable subscriptions.

## Details

A new 'Compression' schema has been introduced, allowing developers to specify a 'compressionAlgorithm' (currently supporting ZLIB) and a 'compressionMode' (COMPRESS or DECOMPRESS). This is accessible via the 'compression' field in 'MessageTransform'. Additionally, the 'BigtableConfig' documentation was updated to clarify that row keys for Pub/Sub-to-Bigtable writes now include a message ID hash (format: subscription name#message ID hash#message ID) to improve data distribution.

**Tags:** `data-transfer` `compression` `bigtable` `pubsub`
