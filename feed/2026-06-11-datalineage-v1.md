---
date: 2026-06-11
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-11  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in SearchLineageStreamingRequest must include the location specified in the parent field.

## Details

The schema for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated to explicitly state that the 'locations' array must contain the location provided in the 'parent' field. While this is a description-only change, it reveals a validation requirement that developers should verify in their request logic to ensure successful streaming searches.

**Tags:** `data-lineage` `documentation`
