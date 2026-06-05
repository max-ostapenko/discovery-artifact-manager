---
date: 2026-06-05
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 3
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-05  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming requests must include the location from the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations array must contain the location specified in the parent field. While this is a description-only change, it likely reflects a backend validation requirement that developers should ensure they are meeting to avoid potential request errors.

**Tags:** `data-lineage` `documentation`
