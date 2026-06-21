---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-streaming", "compression", "bigtable", "pubsub"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces a new Compression schema for message transformations, supporting ZLIB compression and decompression.

## Details

A new `Compression` object has been added to the `MessageTransform` schema. This allows developers to configure `ZLIB` compression or decompression for data streams. Additionally, the `BigtableConfig` documentation was updated to clarify that row keys are constructed using a hash of the message ID (format: `subscription name#message ID hash#message ID`), providing better clarity for those inspecting Bigtable storage directly.

**Tags:** `data-streaming` `compression` `bigtable` `pubsub`
