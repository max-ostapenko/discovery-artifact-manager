---
date: 2026-06-10
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-06-10  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations parameter must contain the location from the parent field. While this is a description-only change, it highlights a specific constraint for developers using the streaming search functionality to ensure their requests are valid and consistent with the parent resource's scope.

**Tags:** `Data Lineage` `Documentation`
