---
date: 2026-05-28
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-catalog"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-05-28  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations array must contain the location provided in the parent field. While this is a description-only change, it likely reflects existing backend validation logic that developers should follow to ensure successful requests.

**Tags:** `documentation` `data-catalog`
