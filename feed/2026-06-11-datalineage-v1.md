---
date: 2026-06-11
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["Data Catalog", "Data Lineage", "API Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-11  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API now explicitly requires that the 'locations' list in streaming search requests includes the location from the 'parent' field.

## Details

A documentation update to the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema clarifies a validation rule for the 'locations' property. Developers must ensure that the location specified in the 'parent' field is also included in the 'locations' array to avoid potential request errors.

**Tags:** `Data Catalog` `Data Lineage` `API Documentation`
