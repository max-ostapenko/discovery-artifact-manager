---
date: 2026-06-05
api: datalineage.v1
service: Data Lineage
title: "Clarification on SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification on SearchLineageStreamingRequest locations

**Date:** 2026-06-05  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A minor documentation update clarifies that the locations field in streaming lineage searches must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated to explicitly state that the locations list must contain the location provided in the parent field. While this is a description-only change, it highlights a specific validation requirement for developers using the streaming search functionality to ensure their requests are correctly formed.

**Tags:** `documentation` `data-lineage`
