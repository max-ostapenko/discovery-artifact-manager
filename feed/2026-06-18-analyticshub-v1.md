---
date: 2026-06-18
api: analyticshub.v1
service: Analytics Hub
title: "ZLIB compression support added to message transforms"
impact: medium
breaking: false
tags: ["data-transfer", "bigtable", "compression", "transformations"]
interesting_score: 6
---

# ZLIB compression support added to message transforms

**Date:** 2026-06-18  
**API:** `analyticshub.v1`  
**Impact:** Medium  

## Summary

Analytics Hub now supports ZLIB compression and decompression for message data transformations, alongside clarified Bigtable row key construction.

## Details

A new 'Compression' schema has been introduced, enabling developers to specify ZLIB as a compression algorithm with modes for both COMPRESS and DECOMPRESS. This is integrated into the 'MessageTransform' resource. Additionally, the documentation for 'BigtableConfig' was updated to clarify that row keys now include a message ID hash (subscription name#message ID hash#message ID), which is a critical detail for ensuring even data distribution across Bigtable nodes.

**Tags:** `data-transfer` `bigtable` `compression` `transformations`
