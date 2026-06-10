---
date: 2026-06-10
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["documentation", "data-lineage"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-10  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations list in streaming requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema has been updated to clarify the requirements for the 'locations' field. Specifically, the list of locations to search in must now explicitly contain the location provided in the 'parent' field. This change helps prevent configuration errors when initiating lineage streaming searches.

**Tags:** `documentation` `data-lineage`
