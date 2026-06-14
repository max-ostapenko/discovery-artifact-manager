---
date: 2026-06-14
api: datalineage.v1
service: Data Lineage
title: "Clarification on SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification on SearchLineageStreamingRequest locations

**Date:** 2026-06-14  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations field in streaming lineage searches must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations array must contain the location value used in the parent field. While this is a description-only change, it likely reflects an existing backend validation requirement for the Data Lineage API that developers should ensure they are meeting to avoid request errors.

**Tags:** `documentation` `data-lineage`
