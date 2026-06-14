---
date: 2026-06-14
api: datalineage.v1
service: Data Lineage
title: "Clarification on SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarification on SearchLineageStreamingRequest locations

**Date:** 2026-06-14  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations has been modified to explicitly state that the list of locations to search in should contain the location provided in the parent field. This is a documentation-only change that clarifies existing validation logic.

**Tags:** `data-lineage` `documentation`
