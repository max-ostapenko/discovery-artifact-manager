---
date: 2026-06-11
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression Support for Message Transformations"
impact: medium
breaking: false
tags: ["pubsub", "bigtable", "compression", "data-sharing"]
interesting_score: 6
---

# ZLIB Compression Support for Message Transformations

**Date:** 2026-06-11  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside clarified Bigtable row key structures.

## Details

A new 'Compression' schema has been introduced, allowing developers to specify 'ZLIB' as an algorithm and choose between 'COMPRESS' or 'DECOMPRESS' modes. This is integrated into the 'MessageTransform' resource, enabling more efficient data handling for Pub/Sub-based subscriptions. Additionally, the documentation for 'BigtableConfig' was updated to reflect that row keys now include a message ID hash (subscription name # message ID hash # message ID), a critical detail for Bigtable performance and hotspot prevention.

**Tags:** `pubsub` `bigtable` `compression` `data-sharing`
