---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, plus clarifies Bigtable row key construction.

## Details

A new `Compression` schema has been introduced, allowing developers to specify `ZLIB` as a compression algorithm and toggle between `COMPRESS` and `DECOMPRESS` modes. This is integrated into the `MessageTransform` resource via the new `compression` property. Additionally, the `BigtableConfig` documentation was updated to reflect that row keys now include a message ID hash (subscription name + message ID hash + message ID), which is a critical detail for Bigtable performance and data distribution.

**Tags:** `data-sharing` `pubsub` `bigtable` `compression`
