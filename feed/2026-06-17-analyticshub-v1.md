---
date: 2026-06-17
api: analyticshub.v1
service: Analytics Hub
title: "New Message Compression Support in Analytics Hub"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "compression"]
interesting_score: 6
---

# New Message Compression Support in Analytics Hub

**Date:** 2026-06-17  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces message transformation capabilities with ZLIB compression and decompression support.

## Details

A new `Compression` schema has been added, which can be utilized within `MessageTransform`. This allows developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). Additionally, the `BigtableConfig` documentation was updated to reflect that row keys now include a message ID hash, improving row key distribution.

**Tags:** `data-sharing` `pubsub` `compression`
