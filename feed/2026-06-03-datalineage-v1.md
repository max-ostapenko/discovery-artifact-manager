---
date: 2026-06-03
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming searches"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming searches

**Date:** 2026-06-03  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in SearchLineageStreamingRequest must include the location specified in the parent field.

## Details

The description for the 'locations' property in the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated. It now explicitly states that the list of locations to search in should contain the location value provided in the 'parent' field. This is a documentation-only change that clarifies existing validation logic.

**Tags:** `Data Lineage` `Documentation`
