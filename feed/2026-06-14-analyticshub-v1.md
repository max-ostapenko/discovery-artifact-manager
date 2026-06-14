---
date: 2026-06-14
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["Analytics Hub", "Data Engineering", "Pub/Sub", "Compression"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-14  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub has introduced a new Compression schema, allowing developers to specify ZLIB compression or decompression during message transformations.

## Details

The update adds a `Compression` object to the `MessageTransform` schema. This new object supports the `ZLIB` algorithm and allows for both `COMPRESS` and `DECOMPRESS` modes. Additionally, the `BigtableConfig` documentation was updated to reflect a change in how row keys are constructed, now including a message ID hash to improve data distribution.

**Tags:** `Analytics Hub` `Data Engineering` `Pub/Sub` `Compression`
