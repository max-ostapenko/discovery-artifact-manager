---
date: 2026-06-03
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreaming locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreaming locations

**Date:** 2026-06-03  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API updated documentation for streaming lineage searches to clarify that the locations list must include the location specified in the parent field.

## Details

A documentation update was made to the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. The locations property description now explicitly states that the list should contain the location provided in the parent field. This ensures consistency between the resource path and the search scope for streaming requests.

**Tags:** `documentation` `data-lineage`
