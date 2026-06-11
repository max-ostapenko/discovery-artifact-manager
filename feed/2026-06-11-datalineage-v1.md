---
date: 2026-06-11
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-11  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the 'locations' field in streaming search requests must include the location specified in the parent field.

## Details

The description for the 'locations' property in the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated. It now explicitly states that the list of locations to search in must contain the location provided in the 'parent' field. This likely reflects a validation requirement that was previously undocumented.

**Tags:** `documentation` `data-lineage`
