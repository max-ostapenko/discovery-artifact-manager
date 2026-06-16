---
date: 2026-06-16
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression support for Message Transformations"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "bigtable", "pubsub"]
interesting_score: 6
---

# ZLIB Compression support for Message Transformations

**Date:** 2026-06-16  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside a clarification on Bigtable subscription row key formats.

## Details

A new `Compression` schema has been introduced, allowing developers to specify `ZLIB` as a `compressionAlgorithm` within a `MessageTransform`. This supports both `COMPRESS` and `DECOMPRESS` modes, enabling more efficient data handling for linked datasets. Additionally, the documentation for `BigtableConfig` was updated to clarify that row keys are constructed using a message ID hash (format: `subscription name#message ID hash#message ID`) to ensure better data distribution.

**Tags:** `data-sharing` `compression` `bigtable` `pubsub`
