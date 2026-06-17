---
date: 2026-06-17
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming search"
impact: low
breaking: false
tags: ["Data Lineage", "API Documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming search

**Date:** 2026-06-17  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API updated its documentation to clarify that the locations list in streaming search requests must include the location from the parent field.

## Details

The update affects the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. The locations property description now explicitly requires that the list contains the location specified in the parent field. This is a documentation-only change but serves as a reminder of existing validation logic for streaming lineage searches.

**Tags:** `Data Lineage` `API Documentation`
