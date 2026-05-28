---
date: 2026-05-28
api: datalineage.v1
service: Data Lineage API
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-05-28  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A minor documentation update clarifies that the locations list in streaming lineage searches must include the location specified in the parent field.

## Details

The description for the locations field in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search in should contain the location provided in the parent field of the request. This is a documentation-only change to clarify existing validation requirements.

**Tags:** `documentation` `data-lineage`
