---
date: 2026-06-15
api: datalineage.v1
service: Data Lineage API
title: "Clarification on SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarification on SearchLineageStreamingRequest locations

**Date:** 2026-06-15  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming lineage searches must include the location specified in the parent field.

## Details

The description for the locations field within the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated. It now explicitly requires that the list of search locations must contain the specific location provided in the request's parent field.

**Tags:** `data-lineage` `documentation`
