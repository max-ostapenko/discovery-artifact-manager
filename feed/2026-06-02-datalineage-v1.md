---
date: 2026-06-02
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming search"
impact: low
breaking: false
tags: ["documentation", "search", "streaming"]
interesting_score: 2
---

# Clarified location requirements for streaming search

**Date:** 2026-06-02  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations array must contain the location provided in the parent field. While this is a description-only change, it highlights a validation requirement that developers should ensure their client code follows to avoid potential request errors when performing streaming lineage searches.

**Tags:** `documentation` `search` `streaming`
