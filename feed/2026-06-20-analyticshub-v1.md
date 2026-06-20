---
date: 2026-06-20
api: analyticshub.v1
service: Analytics Hub
title: "Analytics Hub adds ZLIB compression for message transforms"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "pubsub", "bigtable"]
interesting_score: 6
---

# Analytics Hub adds ZLIB compression for message transforms

**Date:** 2026-06-20  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

New compression and decompression capabilities for message data transformations, plus clarified Bigtable row key formatting.

## Details

The API now includes a Compression schema allowing developers to specify ZLIB as a compression algorithm within MessageTransform. This includes both COMPRESS and DECOMPRESS modes, enabling more efficient handling of message data. Additionally, the BigtableConfig documentation was updated to clarify that row keys are constructed using a hash of the message ID (subscription name#message ID hash#message ID) to ensure better data distribution across Bigtable nodes.

**Tags:** `data-sharing` `compression` `pubsub` `bigtable`
