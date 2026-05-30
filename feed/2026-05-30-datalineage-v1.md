---
date: 2026-05-30
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage search"
impact: low
breaking: false
tags: ["documentation", "search"]
interesting_score: 2
---

# Clarified location requirements for lineage search

**Date:** 2026-05-30  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in SearchLineageStreamingRequest must include the location specified in the parent field.

## Details

The update affects the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. While no functional changes were made to the API surface, the documentation now explicitly states that the locations parameter must contain the location provided in the parent field of the request. This is likely a clarification of existing validation logic rather than a new constraint.

**Tags:** `documentation` `search`
