---
date: 2026-06-16
api: datalineage.v1
service: Data Lineage
title: "Clarification on location requirements for lineage search"
impact: low
breaking: false
tags: ["documentation", "search"]
interesting_score: 2
---

# Clarification on location requirements for lineage search

**Date:** 2026-06-16  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

The Data Lineage API updated documentation for streaming search requests to clarify that the locations list must include the location from the parent field.

## Details

A documentation update was made to the GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema. The locations property description now explicitly states that the list of locations to search in should contain the location provided in the parent field. This doesn't change the API's functionality but clarifies a requirement for successful streaming search requests.

**Tags:** `documentation` `search`
