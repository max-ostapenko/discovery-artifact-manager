---
date: 2026-06-17
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["Analytics Hub", "Pub/Sub", "Bigtable", "Compression"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-17  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Developers can now configure ZLIB compression or decompression for message data within Analytics Hub via a new MessageTransform property.

## Details

A new 'Compression' schema has been introduced, supporting the ZLIB algorithm and both COMPRESS and DECOMPRESS modes. This is integrated into the 'MessageTransform' resource. Additionally, the 'BigtableConfig' documentation was updated to clarify that row keys now include a message ID hash (subscription name # message ID hash # message ID) to improve data distribution.

**Tags:** `Analytics Hub` `Pub/Sub` `Bigtable` `Compression`
