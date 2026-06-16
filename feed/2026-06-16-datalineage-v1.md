---
date: 2026-06-16
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming searches"
impact: low
breaking: false
tags: ["documentation", "data-catalog", "lineage"]
interesting_score: 2
---

# Clarified location requirements for streaming searches

**Date:** 2026-06-16  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in SearchLineageStreamingRequest must include the location specified in the parent field.

## Details

The description for the 'locations' property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search in should contain the location provided in the 'parent' field. This likely reflects an existing validation requirement that was previously missing from the discovery document.

**Tags:** `documentation` `data-catalog` `lineage`
