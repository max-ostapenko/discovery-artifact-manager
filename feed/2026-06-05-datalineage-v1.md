---
date: 2026-06-05
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming search"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming search

**Date:** 2026-06-05  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API updated its documentation to clarify that the locations list in streaming search requests must include the parent location.

## Details

A documentation update was made to the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. The 'locations' field description now explicitly states that the list of locations to search must contain the location specified in the 'parent' field of the request. This likely reflects an existing validation requirement that was previously undocumented.

**Tags:** `data-lineage` `documentation`
