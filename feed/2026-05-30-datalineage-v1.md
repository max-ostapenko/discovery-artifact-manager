---
date: 2026-05-30
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-05-30  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A minor documentation update clarifies that the 'locations' field in streaming lineage searches must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations has been updated. It now explicitly states that the list of locations provided must contain the location value used in the parent field of the request. This helps ensure consistency between the resource path and the search scope.

**Tags:** `documentation` `data-lineage`
