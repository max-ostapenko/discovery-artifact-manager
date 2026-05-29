---
date: 2026-05-29
api: datalineage.v1
service: Data Lineage API
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-05-29  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations must contain the location provided in the parent field, likely reflecting an existing backend validation requirement.

**Tags:** `documentation` `data-lineage`
