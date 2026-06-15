---
date: 2026-06-15
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-15  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for SearchLineageStreamingRequest clarifies that the locations list must include the location specified in the parent field.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest was updated to explicitly state that the list of locations to search in should contain the location from the parent field. This clarifies a requirement for developers using the streaming search functionality to ensure their requests are properly scoped.

**Tags:** `data-lineage` `documentation`
