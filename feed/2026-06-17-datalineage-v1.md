---
date: 2026-06-17
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-17  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location from the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated to explicitly state that the list of locations to search must contain the location provided in the parent field of the request. This clarifies a validation requirement for developers using the streaming search functionality.

**Tags:** `documentation` `data-lineage`
