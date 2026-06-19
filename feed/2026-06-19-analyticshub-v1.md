---
date: 2026-06-19
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression added to Message Transformations"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "pubsub", "bigtable"]
interesting_score: 6
---

# ZLIB Compression added to Message Transformations

**Date:** 2026-06-19  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, enabling more efficient data movement and storage.

## Details

A new 'Compression' schema has been introduced, allowing developers to specify a 'compressionAlgorithm' (currently supporting ZLIB) and a 'compressionMode' (COMPRESS or DECOMPRESS). This configuration is now available as an optional field within the 'MessageTransform' schema. Additionally, the documentation for 'BigtableConfig' was updated to clarify that row keys are constructed using a message ID hash for improved data distribution.

**Tags:** `data-sharing` `compression` `pubsub` `bigtable`
