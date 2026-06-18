---
date: 2026-06-18
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-18  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside updated row key logic for Bigtable subscriptions.

## Details

A new `Compression` schema has been introduced, allowing developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). This is integrated into the `MessageTransform` resource via a new optional `compression` field. Additionally, the documentation for `BigtableConfig` has been updated to reflect a change in row key construction: it now includes a message ID hash between the subscription name and message ID, which is a critical detail for preventing hotspots in Bigtable.

**Tags:** `data-sharing` `pubsub` `bigtable` `compression`
