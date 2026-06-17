---
date: 2026-06-17
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "bigtable", "pubsub"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-17  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside a clarification on Bigtable row key formats.

## Details

A new `Compression` schema has been introduced, allowing developers to specify `ZLIB` as a `compressionAlgorithm` and toggle between `COMPRESS` and `DECOMPRESS` modes. This is integrated into the `MessageTransform` resource via a new optional `compression` field. Additionally, the `BigtableConfig` documentation was updated to reflect that row keys now include a message ID hash (format: `subscription name#message ID hash#message ID`), which is a critical detail for developers querying Bigtable data directly.

**Tags:** `data-sharing` `compression` `bigtable` `pubsub`
