---
date: 2026-06-21
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression support for Message Transformations"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "pubsub", "bigtable"]
interesting_score: 6
---

# ZLIB Compression support for Message Transformations

**Date:** 2026-06-21  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces a new Compression schema for message transformations, allowing ZLIB compression and decompression of data.

## Details

A new 'Compression' object has been added to the 'MessageTransform' schema. This allows developers to specify a 'compressionAlgorithm' (currently supporting ZLIB) and a 'compressionMode' (COMPRESS or DECOMPRESS). Additionally, the 'BigtableConfig' documentation was updated to clarify that row keys are constructed using a message ID hash, which is a standard practice to prevent hotspots in Bigtable.

**Tags:** `data-sharing` `compression` `pubsub` `bigtable`
