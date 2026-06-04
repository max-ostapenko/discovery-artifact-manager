---
date: 2026-06-04
api: datalineage.v1
service: Data Lineage
title: "Clarification on SearchLineageStreaming location requirements"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarification on SearchLineageStreaming location requirements

**Date:** 2026-06-04  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming lineage searches must include the location specified in the parent field.

## Details

The schema for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated to clarify a requirement for the 'locations' field. Developers must ensure that the list of locations provided in the request contains the specific location defined in the 'parent' field. This is a documentation-only change but points to a specific validation requirement for streaming search requests.

**Tags:** `data-lineage` `documentation`
