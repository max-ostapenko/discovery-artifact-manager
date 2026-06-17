---
date: 2026-06-17
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming search"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming search

**Date:** 2026-06-17  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in SearchLineageStreamingRequest must include the location specified in the parent field.

## Details

The description for the 'locations' property in the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated. It now explicitly states that the list of locations to search in should contain the location provided in the 'parent' field. This is a documentation-only change to clarify existing validation logic.

**Tags:** `data-lineage` `documentation`
