---
date: 2026-06-02
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["Data Lineage", "API Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-02  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API now explicitly requires that the locations list in streaming search requests includes the location from the parent field.

## Details

This update modifies the description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations. It clarifies a specific validation requirement for developers using the streaming search functionality: the locations array must contain the location provided in the parent field to ensure consistency between the resource path and the search scope.

**Tags:** `Data Lineage` `API Documentation`
