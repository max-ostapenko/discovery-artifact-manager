---
date: 2026-06-03
api: datalineage.v1
service: Data Lineage
title: "Clarification on SearchLineageStreaming locations"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarification on SearchLineageStreaming locations

**Date:** 2026-06-03  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations array must contain the location value used in the parent field. This ensures consistency between the resource path and the search scope, likely reflecting a validation rule already enforced by the backend.

**Tags:** `data-lineage` `documentation`
