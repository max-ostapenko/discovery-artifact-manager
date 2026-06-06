---
date: 2026-06-06
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-06  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated to be more specific. It now explicitly states that the list of locations to search must contain the location provided in the parent field of the request. This is likely a clarification of existing validation logic rather than a change in API behavior.

**Tags:** `documentation` `data-lineage`
