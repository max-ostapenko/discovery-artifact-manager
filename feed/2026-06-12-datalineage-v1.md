---
date: 2026-06-12
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming search"
impact: low
breaking: false
tags: ["datalineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming search

**Date:** 2026-06-12  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations has been updated to explicitly state that the search locations list must contain the location provided in the parent field. This change clarifies existing validation requirements for developers using the SearchLineageStreaming method.

**Tags:** `datalineage` `documentation`
