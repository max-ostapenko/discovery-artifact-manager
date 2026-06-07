---
date: 2026-06-07
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-06-07  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations field in streaming search requests must include the location from the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated to specify a stricter requirement: the list of locations to search in must contain the location provided in the parent field of the request. While this is a documentation-only change, it likely reflects existing backend validation logic.

**Tags:** `Data Lineage` `Documentation`
