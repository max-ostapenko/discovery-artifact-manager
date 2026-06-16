---
date: 2026-06-16
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support for message transformations"
impact: medium
breaking: false
tags: ["Analytics Hub", "Pub/Sub", "Bigtable", "Data Engineering"]
interesting_score: 6
---

# ZLIB compression support for message transformations

**Date:** 2026-06-16  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, and clarifies Bigtable row key construction.

## Details

A new 'Compression' schema has been added to the API, enabling developers to specify 'compressionAlgorithm' (ZLIB) and 'compressionMode' (COMPRESS or DECOMPRESS) within the 'MessageTransform' resource. This allows for more efficient data handling during message processing. Additionally, the 'BigtableConfig' documentation was updated to clarify that row keys are constructed using a 'message ID hash' alongside the subscription name and message ID, which is a vital detail for understanding data distribution in Bigtable.

**Tags:** `Analytics Hub` `Pub/Sub` `Bigtable` `Data Engineering`
