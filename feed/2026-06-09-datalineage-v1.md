---
date: 2026-06-09
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-06-09  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming lineage searches must include the location specified in the parent field.

## Details

The update affects the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. While no fields were added or removed, the API now explicitly states that the locations array must contain the location provided in the parent field. This clarifies a validation requirement for developers using the streaming search functionality.

**Tags:** `documentation` `data-lineage`
