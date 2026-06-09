---
date: 2026-06-09
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-06-09  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated to explicitly state that the list of locations to search must contain the location provided in the parent field of the request. This clarifies a validation requirement for developers using the streaming search functionality.

**Tags:** `data-lineage` `documentation`
