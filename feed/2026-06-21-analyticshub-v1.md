---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "New Message Compression Support in Analytics Hub"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "pubsub", "bigtable"]
interesting_score: 6
---

# New Message Compression Support in Analytics Hub

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces message transformation capabilities with support for ZLIB compression and decompression.

## Details

A new `Compression` schema has been added to the API, enabling developers to configure `compressionAlgorithm` (supporting ZLIB) and `compressionMode` (COMPRESS or DECOMPRESS) within the `MessageTransform` property. This allows for more efficient data handling during message processing. Additionally, the documentation for `BigtableConfig` was updated to clarify that row keys are constructed using the subscription name, a message ID hash, and the message ID, which is a critical detail for anyone querying the underlying Bigtable storage directly.

**Tags:** `data-sharing` `compression` `pubsub` `bigtable`
