---
date: 2026-06-21
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["data-catalog", "lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-06-21  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations field in lineage search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations list must contain the location provided in the parent field. While this is a description-only change, it highlights a functional requirement for successful streaming search requests that may have been previously ambiguous to developers.

**Tags:** `data-catalog` `lineage` `documentation`
