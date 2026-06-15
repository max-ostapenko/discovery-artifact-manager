---
date: 2026-06-15
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB Compression support for Message Transformations"
impact: medium
breaking: false
tags: ["data-sharing", "compression", "transformations"]
interesting_score: 6
---

# ZLIB Compression support for Message Transformations

**Date:** 2026-06-15  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub introduces a new Compression schema for message transformations, allowing developers to specify ZLIB compression or decompression modes.

## Details

A new Compression object has been added to the MessageTransform schema. This allows for the configuration of message data processing using the ZLIB algorithm in either COMPRESS or DECOMPRESS modes. Additionally, the BigtableConfig documentation was updated to clarify that row keys are constructed using the subscription name, a message ID hash, and the message ID, delimited by hashes.

**Tags:** `data-sharing` `compression` `transformations`
