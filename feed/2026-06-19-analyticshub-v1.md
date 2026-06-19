---
date: 2026-06-19
api: analyticshub.v1
service: Analytics Hub
title: "Compression support for Message Transformations"
impact: medium
breaking: false
tags: ["data-sharing", "pubsub", "bigtable", "compression"]
interesting_score: 6
---

# Compression support for Message Transformations

**Date:** 2026-06-19  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression within message transformations, alongside a clarification on Bigtable row key structures.

## Details

A new `Compression` schema has been added to the API, allowing developers to specify a `compressionAlgorithm` (currently supporting `ZLIB`) and a `compressionMode` (`COMPRESS` or `DECOMPRESS`). This is exposed via the `compression` field in the `MessageTransform` resource. Additionally, the `BigtableConfig` description was updated to reflect that row keys are composed of the subscription name, a message ID hash, and the message ID, which is a more specific definition than previously documented.

**Tags:** `data-sharing` `pubsub` `bigtable` `compression`
