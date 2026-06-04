---
date: 2026-06-04
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "search", "validation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-04  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations array must contain the location provided in the parent field. While this is a description-only change, it likely reflects an existing backend validation requirement that was previously undocumented, helping developers avoid potential request errors.

**Tags:** `documentation` `search` `validation`
