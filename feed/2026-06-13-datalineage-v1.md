---
date: 2026-06-13
api: datalineage.v1
service: Data Lineage
title: "Clarification on location requirements for lineage search"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification on location requirements for lineage search

**Date:** 2026-06-13  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API updated documentation for streaming search requests to clarify that the search locations list must include the location specified in the parent field.

## Details

The description for the locations field in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest now explicitly states that the list should contain the location from the parent field. This is a documentation-only update to clarify existing requirements for the SearchLineageStreaming method, helping developers avoid potential configuration errors.

**Tags:** `documentation` `data-lineage`
