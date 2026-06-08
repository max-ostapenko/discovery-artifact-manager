---
date: 2026-06-08
api: datalineage.v1
service: Data Lineage
title: "Clarification on SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification on SearchLineageStreamingRequest locations

**Date:** 2026-06-08  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming lineage searches must include the location specified in the parent field.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search must contain the location provided in the parent field of the request. This doesn't change the API schema but clarifies usage requirements for developers implementing streaming lineage searches to ensure requests are valid.

**Tags:** `documentation` `data-lineage`
