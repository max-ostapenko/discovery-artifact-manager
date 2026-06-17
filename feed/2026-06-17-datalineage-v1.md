---
date: 2026-06-17
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming searches"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming searches

**Date:** 2026-06-17  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for SearchLineageStreamingRequest clarifies that the locations list must include the location specified in the parent field.

## Details

The description for the locations field in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated to explicitly state that the list of search locations must contain the location provided in the parent field. This is a documentation-only change that clarifies existing validation logic.

**Tags:** `data-lineage` `documentation`
