---
date: 2026-06-18
api: datalineage.v1
service: Data Lineage API
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-18  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations field in streaming search requests must include the location specified in the parent field.

## Details

The schema for GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated to clarify the requirements for the 'locations' property. It now explicitly states that this list should contain the location provided in the 'parent' field. While this is a description-only change, it likely reflects existing backend validation logic that developers should ensure they are following.

**Tags:** `data-lineage` `documentation`
