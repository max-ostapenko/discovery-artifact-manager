---
date: 2026-06-20
api: analyticshub.v1
service: Analytics Hub
title: "Message compression support for data transforms"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "pubsub", "bigtable"]
interesting_score: 6
---

# Message compression support for data transforms

**Date:** 2026-06-20  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces a new Compression schema for message transformations, supporting ZLIB compression and decompression.

## Details

A new `MessageTransform` property now includes an optional `compression` field. This field utilizes the new `Compression` object, which allows developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). Additionally, the documentation for `BigtableConfig` was updated to clarify that row keys now include a message ID hash, which is a standard practice for better data distribution in Bigtable.

**Tags:** `data-sharing` `compression` `pubsub` `bigtable`
