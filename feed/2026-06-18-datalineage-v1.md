---
date: 2026-06-18
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-18  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search in should contain the location provided in the parent field of the request. This is a documentation-only change to ensure consistency between the parent resource and the search scope.

**Tags:** `documentation` `data-lineage`
