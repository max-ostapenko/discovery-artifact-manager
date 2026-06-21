---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside a clarification on Bigtable row key generation.

## Details

A new `Compression` schema has been added, allowing developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). This is exposed via the new `compression` field in the `MessageTransform` resource. Additionally, the documentation for `BigtableConfig` was updated to clarify that row keys for Bigtable subscriptions now include a message ID hash (format: `subscription name#message ID hash#message ID`) to improve data distribution.

**Tags:** `data-sharing` `pubsub` `bigtable` `compression`
