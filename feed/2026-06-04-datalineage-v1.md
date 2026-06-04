---
date: 2026-06-04
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreaming locations"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarification for SearchLineageStreaming locations

**Date:** 2026-06-04  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations field must include the location specified in the parent field.

## Details

The description for the locations property in the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated. It now explicitly states that the list of locations to search in must contain the location provided in the parent field. This is a documentation-only change to clarify existing validation requirements.

**Tags:** `documentation` `data-lineage`
