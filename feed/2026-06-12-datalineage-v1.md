---
date: 2026-06-12
api: datalineage.v1
service: Data Lineage API
title: "Clarification for SearchLineageStreamingRequest locations"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarification for SearchLineageStreamingRequest locations

**Date:** 2026-06-12  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The description for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest.locations was updated to explicitly state that the list of locations to search must contain the location provided in the parent field of the request. This is a clarification of existing requirements rather than a change in API behavior.

**Tags:** `Data Lineage` `Documentation`
