---
date: 2026-06-06
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-06  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API now explicitly requires that the 'locations' list in streaming search requests includes the location specified in the 'parent' field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations has been updated to clarify a validation requirement. When performing a streaming lineage search, the locations array must contain the specific location defined in the request's parent field. This doesn't change the API surface but helps prevent validation errors for developers by making the relationship between the parent resource and search scope explicit.

**Tags:** `Data Lineage` `Documentation`
