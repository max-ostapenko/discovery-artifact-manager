---
date: 2026-06-18
api: analyticshub.v1
service: Analytics Hub
title: "Message compression support added to transformations"
impact: medium
breaking: false
tags: ["pubsub", "bigtable", "compression", "data-sharing"]
interesting_score: 6
---

# Message compression support added to transformations

**Date:** 2026-06-18  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, allowing for more efficient data handling and reduced storage costs.

## Details

A new 'Compression' schema has been introduced, featuring 'compressionAlgorithm' (supporting ZLIB) and 'compressionMode' (COMPRESS or DECOMPRESS). This schema is now available as an optional field within 'MessageTransform'. Additionally, the 'BigtableConfig' documentation was updated to reflect a change in row key construction, which now includes a message ID hash for better indexing and distribution.

**Tags:** `pubsub` `bigtable` `compression` `data-sharing`
