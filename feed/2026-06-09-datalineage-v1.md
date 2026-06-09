---
date: 2026-06-09
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-06-09  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming lineage searches must include the location specified in the parent field.

## Details

The description for the locations field within the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated. It now explicitly requires that the list of locations to search must contain the specific location provided in the parent field of the request. This is a documentation-only change to clarify existing API requirements.

**Tags:** `data-lineage` `documentation`
