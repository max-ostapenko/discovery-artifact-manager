---
date: 2026-06-15
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-engineering", "pubsub", "compression"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-15  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression for message data transformations.

## Details

A new `Compression` schema has been added to the API, allowing developers to specify a `compressionAlgorithm` (currently `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). This is exposed via the new `compression` field in the `MessageTransform` object. Additionally, the `BigtableConfig` documentation was updated to clarify that row keys are constructed using a subscription name, message ID hash, and message ID for better data distribution.

**Tags:** `data-engineering` `pubsub` `compression`
