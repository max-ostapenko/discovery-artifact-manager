---
date: 2026-06-03
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-06-03  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A minor documentation update clarifies that the locations list in streaming search requests must include the location from the parent field.

## Details

The description for the locations field in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search must contain the location provided in the parent field of the request. This doesn't change the API surface but helps prevent validation errors for developers using the streaming search functionality.

**Tags:** `documentation` `data-lineage`
