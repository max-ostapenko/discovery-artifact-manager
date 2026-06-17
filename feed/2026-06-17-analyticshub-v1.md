---
date: 2026-06-17
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["data-transformation", "bigtable", "compression", "pubsub"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-17  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside updated documentation for Bigtable row key formats.

## Details

A new Compression schema has been introduced, allowing developers to specify ZLIB as a compressionAlgorithm and choose between COMPRESS or DECOMPRESS modes. This is integrated into the MessageTransform resource via a new optional compression field. Additionally, the BigtableConfig description was updated to clarify that row keys are constructed using the subscription name, a message ID hash, and the message ID delimited by #.

**Tags:** `data-transformation` `bigtable` `compression` `pubsub`
