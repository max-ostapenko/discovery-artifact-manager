---
date: 2026-06-14
api: datalineage.v1
service: Data Lineage API
title: "Clarified location requirements for streaming searches"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming searches

**Date:** 2026-06-14  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in SearchLineageStreamingRequest must include the location specified in the parent field.

## Details

The description for the 'locations' field in the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated. It now explicitly states that the list of locations to search must contain the location provided in the 'parent' field of the request. This is likely a clarification of existing validation logic rather than a change in API behavior.

**Tags:** `data-lineage` `documentation`
