---
date: 2026-06-18
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression Support for Message Transformations"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "bigtable", "pubsub"]
interesting_score: 6
---

# ZLIB Compression Support for Message Transformations

**Date:** 2026-06-18  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression for message data via a new MessageTransform configuration.

## Details

A new `Compression` schema has been introduced, which can be applied to `MessageTransform`. This allows developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). Additionally, documentation for `BigtableConfig` was updated to clarify that row keys now include a message ID hash, improving data distribution for Bigtable-backed subscriptions.

**Tags:** `data-sharing` `compression` `bigtable` `pubsub`
