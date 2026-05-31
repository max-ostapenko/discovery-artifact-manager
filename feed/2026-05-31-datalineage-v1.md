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

A documentation update clarifies that the 'locations' field in streaming lineage searches must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated. It now explicitly states that the list of locations to search in should contain the location provided in the parent field of the request. This ensures that the search scope is consistent with the resource hierarchy defined in the parent path.

**Tags:** `documentation` `data-lineage`
