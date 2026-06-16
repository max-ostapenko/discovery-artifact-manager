---
date: 2026-06-16
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-16  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations parameter must contain the location provided in the parent field. While this is a description-only change, it highlights a functional requirement for developers using the streaming search API to ensure their requests are valid.

**Tags:** `documentation` `data-lineage`
