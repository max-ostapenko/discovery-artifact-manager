---
date: 2026-06-12
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "pubsub", "bigtable"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-12  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, allowing for more efficient data handling in message-based subscriptions.

## Details

A new 'Compression' schema has been added to the API, enabling developers to specify a 'compressionAlgorithm' (currently supporting ZLIB) and a 'compressionMode' (COMPRESS or DECOMPRESS). This is integrated into 'MessageTransform', which is used to modify data as it flows through the service. Additionally, the 'BigtableConfig' documentation was updated to clarify that row keys now include a message ID hash, likely to improve partition distribution and avoid hotspots.

**Tags:** `data-sharing` `compression` `pubsub` `bigtable`
