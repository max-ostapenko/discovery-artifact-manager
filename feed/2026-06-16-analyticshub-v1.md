---
date: 2026-06-16
api: analyticshub.v1
service: Analytics Hub
title: "Message Compression and Bigtable Row Key Clarification"
impact: medium
breaking: false
tags: ["data-transfer", "compression", "bigtable", "pubsub"]
interesting_score: 6
---

# Message Compression and Bigtable Row Key Clarification

**Date:** 2026-06-16  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces message transformation capabilities with ZLIB compression support and clarifies Bigtable subscription row key structures.

## Details

A new `Compression` schema has been added to the API, enabling ZLIB compression and decompression via the `MessageTransform` property. This allows for more efficient data handling during message processing. Additionally, the documentation for `BigtableConfig` was updated to specify that row keys are constructed using the subscription name, a message ID hash, and the message ID, delimited by `#`.

**Tags:** `data-transfer` `compression` `bigtable` `pubsub`
