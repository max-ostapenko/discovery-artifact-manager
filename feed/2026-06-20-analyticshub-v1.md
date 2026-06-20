---
date: 2026-06-20
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["data-transfer", "compression", "pubsub", "bigtable"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-20  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Developers can now configure ZLIB compression and decompression within message transformations to optimize data transfer.

## Details

A new 'Compression' schema has been added to the API, supporting the ZLIB algorithm. This is exposed via the 'MessageTransform' resource, allowing users to specify whether to 'COMPRESS' or 'DECOMPRESS' data payloads. Additionally, the 'BigtableConfig' documentation was updated to reflect a change in row key construction, which now includes a message ID hash for better data distribution.

**Tags:** `data-transfer` `compression` `pubsub` `bigtable`
