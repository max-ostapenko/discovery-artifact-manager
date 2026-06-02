---
date: 2026-06-02
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-02  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming search requests must include the location from the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated to explicitly state that the list should contain the location specified in the parent field. While this is a documentation-only change, it likely reflects a validation rule that developers should adhere to when using the SearchLineageStreaming method.

**Tags:** `Data Lineage` `Documentation`
