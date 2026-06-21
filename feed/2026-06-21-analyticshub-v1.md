---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds Message Compression support"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "compression"]
interesting_score: 6
---

# Analytics Hub adds Message Compression support

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression for message transformations.

## Details

A new `Compression` schema has been added to `MessageTransform`, allowing developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). Additionally, the documentation for `BigtableConfig` was updated to clarify that the row key format now includes a message ID hash between the subscription name and message ID.

**Tags:** `data-sharing` `pubsub` `compression`
