---
date: 2026-06-19
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression Support for Message Transforms"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# ZLIB Compression Support for Message Transforms

**Date:** 2026-06-19  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub adds support for ZLIB compression and decompression within message transformations, plus a refined row key format for Bigtable subscriptions.

## Details

A new 'Compression' schema has been introduced, allowing developers to specify 'ZLIB' as an algorithm and choose between 'COMPRESS' or 'DECOMPRESS' modes. This is integrated into 'MessageTransform' via the new 'compression' property, enabling more efficient data handling for message-based subscriptions. Additionally, the 'BigtableConfig' documentation clarifies that row keys now include a message ID hash (subscription name # message ID hash # message ID), which likely improves data distribution across Bigtable nodes.

**Tags:** `data-sharing` `pubsub` `bigtable` `compression`
