---
date: 2026-06-20
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-20  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside clarified row key formats for Bigtable subscriptions.

## Details

A new `Compression` schema has been added, allowing developers to specify `ZLIB` as a compression algorithm with modes for either `COMPRESS` or `DECOMPRESS`. This is now available as an optional `compression` field within the `MessageTransform` resource. Additionally, the documentation for `BigtableConfig` was updated to reflect that row keys now include a message ID hash (format: `subscription name#message ID hash#message ID`), which is a critical detail for Bigtable performance and hotspot prevention.

**Tags:** `data-sharing` `pubsub` `bigtable` `compression`
