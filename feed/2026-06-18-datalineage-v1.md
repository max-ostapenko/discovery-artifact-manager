---
date: 2026-06-18
api: datalineage.v1
service: Data Lineage
title: "Clarified Location Requirements for Lineage Search"
impact: low
breaking: false
tags: ["documentation", "search"]
interesting_score: 2
---

# Clarified Location Requirements for Lineage Search

**Date:** 2026-06-18  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming search requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema now explicitly states that the locations parameter must contain the location provided in the parent field. While this is a description-only change, it likely reflects an existing backend validation requirement for the SearchLineageStreaming method that developers should ensure they are meeting.

**Tags:** `documentation` `search`
