---
date: 2026-05-30
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreaming locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreaming locations

**Date:** 2026-05-30  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the 'locations' list in streaming search requests must include the location specified in the 'parent' field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated to clarify the usage of the locations field. Developers must ensure that the list of locations provided in this field includes the specific location defined in the parent resource path. While this appears to be a documentation-only change, it likely reflects an existing backend validation requirement.

**Tags:** `documentation` `data-lineage`
