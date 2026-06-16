---
date: 2026-06-16
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression support for Message Transformations"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "compression", "bigtable"]
interesting_score: 6
---

# ZLIB Compression support for Message Transformations

**Date:** 2026-06-16  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, providing more control over data payloads.

## Details

A new 'Compression' schema has been introduced, which can be applied via the 'MessageTransform' property. It supports the ZLIB algorithm and allows developers to explicitly set the mode to either COMPRESS or DECOMPRESS. Additionally, the 'BigtableConfig' documentation was updated to clarify that row keys are constructed using a message ID hash, which is a critical detail for Bigtable performance and hotspot avoidance.

**Tags:** `data-sharing` `pubsub` `compression` `bigtable`
