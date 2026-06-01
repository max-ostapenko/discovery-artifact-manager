---
date: 2026-06-01
api: datalineage.v1
service: Data Lineage
title: "Clarification on location requirements for lineage search"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification on location requirements for lineage search

**Date:** 2026-06-01  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations property must contain the location provided in the parent field. This is likely a clarification of existing backend validation logic rather than a functional change to the API surface, helping developers avoid potential validation errors.

**Tags:** `documentation` `data-lineage`
