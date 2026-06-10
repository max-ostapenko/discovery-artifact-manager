---
date: 2026-06-10
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-06-10  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated. It now explicitly states that the list of locations to search must contain the location provided in the parent field. This helps prevent potential validation errors when performing streaming lineage searches by ensuring consistency between the parent resource path and the search scope.

**Tags:** `data-lineage` `documentation`
