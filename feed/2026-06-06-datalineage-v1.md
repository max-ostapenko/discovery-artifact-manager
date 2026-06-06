---
date: 2026-06-06
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["Data Lineage", "Data Catalog", "Search"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-06  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The schema for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated to clarify a validation requirement. Specifically, the 'locations' field must now explicitly contain the location defined in the 'parent' field of the request. This change likely reflects an existing backend enforcement that was previously undocumented.

**Tags:** `Data Lineage` `Data Catalog` `Search`
