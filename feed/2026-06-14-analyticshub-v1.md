---
date: 2026-06-14
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-14  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside updated row key logic for Bigtable subscriptions.

## Details

A new `Compression` schema has been introduced, allowing developers to configure `ZLIB` compression or decompression via the `MessageTransform` resource. This enables more efficient data handling for message-based workflows. Additionally, the `BigtableConfig` documentation was updated to clarify that row keys now include a message ID hash (format: `subscription name#message ID hash#message ID`), which is a critical detail for Bigtable performance and hotspot avoidance.

**Tags:** `data-sharing` `pubsub` `bigtable` `compression`
