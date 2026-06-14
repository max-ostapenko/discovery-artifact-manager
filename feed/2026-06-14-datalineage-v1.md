---
date: 2026-06-14
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-catalog"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-14  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations parameter must contain the location provided in the parent field. This is a documentation-only change to clarify existing requirements for the SearchLineageStreaming method.

**Tags:** `documentation` `data-catalog`
