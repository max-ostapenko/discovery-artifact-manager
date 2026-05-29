---
date: 2026-05-29
api: datalineage.v1
service: Data Lineage API
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-05-29  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A minor documentation update clarifies that the 'locations' field in streaming lineage searches must include the location specified in the 'parent' field.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations provided must contain the specific location defined in the parent field of the request. This doesn't change the API behavior but helps avoid validation errors for developers using the streaming search functionality.

**Tags:** `documentation` `data-lineage`
