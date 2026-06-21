---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["data-pipelines", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces message compression and decompression capabilities for data pipelines, alongside updated Bigtable row key logic.

## Details

A new `Compression` schema has been added to the API, supporting the `ZLIB` algorithm with both `COMPRESS` and `DECOMPRESS` modes. This is exposed via the `compression` field in `MessageTransform`. Additionally, the documentation for `BigtableConfig` was updated to clarify that row keys now include a message ID hash (format: `subscription name#message ID hash#message ID`), which is a standard practice to prevent hotspotting in Bigtable.

**Tags:** `data-pipelines` `pubsub` `bigtable` `compression`
