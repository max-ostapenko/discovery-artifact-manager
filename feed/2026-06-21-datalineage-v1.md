---
date: 2026-06-21
api: datalineage.v1
service: Data Lineage
title: "Clarified Location Requirements for Lineage Search"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified Location Requirements for Lineage Search

**Date:** 2026-06-21  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The description for the locations field in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search in must contain the location provided in the parent field. This likely reflects an existing backend validation rule that was previously missing from the discovery document.

**Tags:** `data-lineage` `documentation`
