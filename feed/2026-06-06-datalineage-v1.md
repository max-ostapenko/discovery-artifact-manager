---
date: 2026-06-06
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "search"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-06  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A minor documentation update clarifies that the locations field in lineage streaming requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated to explicitly state that the locations array must contain the location provided in the parent field. This ensures consistency between the resource path and the search scope, likely reflecting an existing validation rule.

**Tags:** `documentation` `search`
