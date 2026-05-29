---
date: 2026-05-29
api: datalineage.v1
service: Data Lineage API
title: "Clarified location requirements for streaming searches"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming searches

**Date:** 2026-05-29  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API now explicitly requires that the locations list in streaming search requests includes the location specified in the parent field.

## Details

A documentation update was made to the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. The 'locations' property description now specifies that the list must contain the location from the 'parent' field. This is a clarification of existing validation logic rather than a change to the API surface itself.

**Tags:** `data-lineage` `documentation`
