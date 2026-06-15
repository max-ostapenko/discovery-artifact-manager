---
date: 2026-06-15
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreaming locations"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarification for SearchLineageStreaming locations

**Date:** 2026-06-15  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming lineage searches must include the location specified in the parent field.

## Details

The description for the locations field in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations provided must contain the specific location defined in the request's parent field. This is a documentation-only change to clarify existing validation requirements.

**Tags:** `data-lineage` `documentation`
