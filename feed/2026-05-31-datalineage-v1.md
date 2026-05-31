---
date: 2026-05-31
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-05-31  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API now explicitly requires that the locations list in streaming search requests includes the location specified in the parent field.

## Details

A documentation update to GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest clarifies that the locations property must contain the location provided in the parent field. While this doesn't change the API schema, it highlights a validation requirement for developers using the SearchLineageStreaming method to avoid potential request errors.

**Tags:** `documentation` `data-lineage`
