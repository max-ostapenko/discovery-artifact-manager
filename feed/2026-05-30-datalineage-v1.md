---
date: 2026-05-30
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-05-30  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in SearchLineageStreamingRequest must include the location from the parent field.

## Details

The description for the `locations` field in the `GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest` schema has been updated. It now explicitly requires that the list of locations to search must contain the specific location provided in the `parent` field of the request. This likely reflects a validation requirement that was previously undocumented.

**Tags:** `documentation` `data-lineage`
