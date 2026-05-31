---
date: 2026-05-31
api: datalineage.v1
service: Data Lineage API
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-05-31  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The documentation for the locations field in SearchLineageStreamingRequest now explicitly requires the location from the parent field to be included.

## Details

A minor documentation update was made to the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. The description for the 'locations' property now clarifies that the list should contain the specific location provided in the 'parent' field. This ensures that the search scope is consistent with the resource hierarchy.

**Tags:** `documentation` `data-lineage`
