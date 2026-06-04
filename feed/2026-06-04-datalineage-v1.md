---
date: 2026-06-04
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-06-04  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations field in streaming lineage search requests must include the location specified in the parent field.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations provided should contain the location from the parent field. This is a documentation-only change that clarifies existing validation logic rather than a change to the API's functional behavior.

**Tags:** `documentation` `data-lineage`
