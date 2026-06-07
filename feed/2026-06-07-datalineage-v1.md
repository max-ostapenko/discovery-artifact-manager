---
date: 2026-06-07
api: datalineage.v1
service: Data Lineage
title: "Clarified Location Requirements for Lineage Streaming"
impact: low
breaking: false
tags: ["data-lineage", "documentation"]
interesting_score: 2
---

# Clarified Location Requirements for Lineage Streaming

**Date:** 2026-06-07  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations parameter must contain the location value provided in the parent field. While this is a description-only change, it highlights a specific validation requirement for developers using the streaming search functionality to avoid potential request errors.

**Tags:** `data-lineage` `documentation`
