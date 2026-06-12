---
date: 2026-06-12
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression Support for Message Transforms"
impact: medium
breaking: false
tags: ["data-transfer", "compression", "pubsub"]
interesting_score: 6
---

# ZLIB Compression Support for Message Transforms

**Date:** 2026-06-12  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression for message data via a new MessageTransform property.

## Details

Developers can now configure `MessageTransform` with a new `compression` object. This schema allows for specifying a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (either `COMPRESS` or `DECOMPRESS`). This addition suggests tighter integration with Pub/Sub-style message processing where payload size optimization is critical. Additionally, the `BigtableConfig` documentation was updated to clarify that row keys are constructed using a subscription name, a message ID hash, and the message ID.

**Tags:** `data-transfer` `compression` `pubsub`
