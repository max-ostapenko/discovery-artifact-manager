---
date: 2026-06-09
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-06-09  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The update affects GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest. While no functional code changes were made, the API documentation now explicitly states that the locations array must contain the location provided in the parent field. This helps prevent validation errors for developers implementing streaming lineage searches by ensuring consistency between the parent resource path and the search scope.

**Tags:** `documentation` `data-lineage`
