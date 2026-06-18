---
date: 2026-06-18
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-18  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside a refined row key format for Bigtable subscriptions.

## Details

A new `Compression` schema has been added to the API, enabling developers to specify `compressionAlgorithm` (currently supporting `ZLIB`) and `compressionMode` (`COMPRESS` or `DECOMPRESS`). This is exposed via the `MessageTransform` resource. Additionally, the `BigtableConfig` documentation was updated to clarify that row keys now include a message ID hash (format: `subscription name#message ID hash#message ID`), which is a standard practice to prevent hotspots in Bigtable.

**Tags:** `data-sharing` `pubsub` `bigtable` `compression`
