---
date: 2026-06-13
api: datalineage.v1
service: Data Lineage API
title: "Clarified location requirements for streaming searches"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming searches

**Date:** 2026-06-13  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API documentation now explicitly requires that the locations list in streaming search requests includes the parent location.

## Details

A documentation update was made to the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. The 'locations' property description now specifies that the list of search locations must contain the location provided in the 'parent' field of the request. This clarifies validation logic for developers using the streaming search endpoint.

**Tags:** `data-lineage` `documentation`
