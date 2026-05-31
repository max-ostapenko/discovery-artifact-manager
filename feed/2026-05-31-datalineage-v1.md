---
date: 2026-05-31
api: datalineage.v1
service: Data Lineage
title: "Clarification on SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarification on SearchLineageStreamingRequest locations

**Date:** 2026-05-31  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in SearchLineageStreamingRequest must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations now explicitly states that the list should contain the location from the parent field. While this is a documentation-only change, it likely reflects a backend validation requirement that developers need to follow to avoid request errors when searching lineage data.

**Tags:** `data-lineage` `documentation`
