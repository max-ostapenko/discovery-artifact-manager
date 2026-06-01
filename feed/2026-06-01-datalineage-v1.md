---
date: 2026-06-01
api: datalineage.v1
service: Data Lineage
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["documentation", "data-catalog"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-06-01  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A minor documentation update clarifies that the locations field must include the location specified in the parent field for streaming lineage searches.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations should contain the location provided in the parent field. This is a documentation-only change to help developers correctly configure streaming search requests.

**Tags:** `documentation` `data-catalog`
