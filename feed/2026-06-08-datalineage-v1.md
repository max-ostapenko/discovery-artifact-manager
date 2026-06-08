---
date: 2026-06-08
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-06-08  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search in should contain the specific location provided in the parent field. This is a documentation-only change that clarifies existing validation logic for developers using the streaming search capability.

**Tags:** `Data Lineage` `Documentation`
