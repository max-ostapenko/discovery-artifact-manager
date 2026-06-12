---
date: 2026-06-12
api: datalineage.v1
service: Data Lineage
title: "Clarified Location Requirements for Lineage Streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified Location Requirements for Lineage Streaming

**Date:** 2026-06-12  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations array must contain the location provided in the parent field. While this doesn't change the API surface, it clarifies a requirement that likely triggers validation errors if not followed.

**Tags:** `documentation` `data-lineage`
