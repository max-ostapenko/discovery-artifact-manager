---
date: 2026-06-04
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for streaming searches"
impact: low
breaking: false
tags: ["datalineage", "documentation"]
interesting_score: 2
---

# Clarified location requirements for streaming searches

**Date:** 2026-06-04  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the 'locations' field in streaming lineage searches must include the location specified in the 'parent' field.

## Details

The description for the 'locations' property in the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated. It now explicitly states that the list of locations must contain the location provided in the 'parent' field. This is a documentation-only change but highlights a strict validation requirement for developers using the streaming search API.

**Tags:** `datalineage` `documentation`
