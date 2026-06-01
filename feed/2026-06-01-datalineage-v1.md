---
date: 2026-06-01
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "search"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-01  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location from the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations parameter must contain the location specified in the parent field. This ensures consistency between the resource path and the search scope during streaming lineage searches.

**Tags:** `documentation` `search`
