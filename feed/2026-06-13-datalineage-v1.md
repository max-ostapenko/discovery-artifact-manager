---
date: 2026-06-13
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 3
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-13  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for SearchLineageStreamingRequest clarifies that the locations list must include the location specified in the parent field.

## Details

The description for the locations field in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search in should contain the location provided in the parent field. While this is technically a documentation-only change, it likely reflects a backend validation requirement that developers should ensure they are meeting to avoid potential request errors.

**Tags:** `documentation` `data-lineage`
