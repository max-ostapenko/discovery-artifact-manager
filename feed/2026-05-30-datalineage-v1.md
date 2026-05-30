---
date: 2026-05-30
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreaming locations"
impact: low
breaking: false
tags: ["documentation", "data-catalog"]
interesting_score: 2
---

# Clarification for SearchLineageStreaming locations

**Date:** 2026-05-30  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the 'locations' field in streaming lineage searches must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated to clarify the usage of the locations field. While already marked as required, the documentation now explicitly states that this list should contain the location provided in the parent field of the request. This ensures consistency between the resource path and the search scope.

**Tags:** `documentation` `data-catalog`
