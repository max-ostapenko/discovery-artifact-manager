---
date: 2026-06-09
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming search"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming search

**Date:** 2026-06-09  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The description for the 'locations' field in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that this list must contain the location from the 'parent' field. This is a documentation-only change, but it reveals a specific validation requirement for developers using the streaming search functionality.

**Tags:** `data-lineage` `documentation`
