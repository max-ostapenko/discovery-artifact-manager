---
date: 2026-06-12
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming search"
impact: low
breaking: false
tags: ["Data Lineage", "API Documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming search

**Date:** 2026-06-12  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API now explicitly requires that the locations list in streaming search requests includes the location specified in the parent field.

## Details

The update modifies the description for the locations property within the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. Developers using SearchLineageStreaming should ensure their locations array is consistent with the parent field to align with this clarified validation requirement.

**Tags:** `Data Lineage` `API Documentation`
