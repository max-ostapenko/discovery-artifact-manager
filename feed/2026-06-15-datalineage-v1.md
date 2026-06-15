---
date: 2026-06-15
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming searches"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for streaming searches

**Date:** 2026-06-15  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations field in streaming lineage searches must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema's description for the locations field has been updated. It now explicitly states that the list of locations to search in must contain the specific location provided in the parent field. This clarifies a validation requirement for developers implementing streaming lineage lookups.

**Tags:** `documentation` `data-lineage`
