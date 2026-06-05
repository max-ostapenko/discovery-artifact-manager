---
date: 2026-06-05
api: datalineage.v1
service: Data Lineage API
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-05  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated to explicitly state that the locations list should contain the location from the parent field. This is a documentation-only change that likely reflects existing backend validation requirements for the SearchLineageStreaming method.

**Tags:** `Data Lineage` `Documentation`
