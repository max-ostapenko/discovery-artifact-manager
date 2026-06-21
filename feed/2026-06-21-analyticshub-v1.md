---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "Message Compression for Analytics Hub Transforms"
impact: medium
breaking: false
tags: ["Analytics Hub", "Data Engineering", "Bigtable", "Compression"]
interesting_score: 6
---

# Message Compression for Analytics Hub Transforms

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces a new Compression schema for message transforms, supporting ZLIB compression and decompression.

## Details

A new `Compression` object has been added to the `MessageTransform` schema. This allows developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (either `COMPRESS` or `DECOMPRESS`). Additionally, the documentation for `BigtableConfig` was updated to clarify that row keys are constructed using a subscription name, message ID hash, and message ID, which helps in understanding data distribution and avoiding hotspots.

**Tags:** `Analytics Hub` `Data Engineering` `Bigtable` `Compression`
