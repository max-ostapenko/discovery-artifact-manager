---
date: 2026-06-05
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-05  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for SearchLineageStreamingRequest clarifies that the locations list must include the location specified in the parent field.

## Details

The description for the locations property in GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest has been updated. It now explicitly states that the list of locations to search in should contain the location provided in the parent field. This is a clarification of existing validation requirements rather than a functional change to the API schema.

**Tags:** `data-lineage` `documentation`
