---
date: 2026-06-11
api: datalineage.v1
service: Data Lineage
title: "Clarified location requirements for lineage streaming"
impact: low
breaking: false
tags: ["Data Lineage", "Documentation"]
interesting_score: 2
---

# Clarified location requirements for lineage streaming

**Date:** 2026-06-11  
**API:** `datalineage.v1`  
**Impact:** Low  

## Summary

A documentation update for the Data Lineage API clarifies that the locations field in streaming requests must include the location specified in the parent field.

## Details

The GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest schema's locations property description was updated. It now explicitly states that the list of locations to search must contain the location provided in the parent field. This clarifies a validation requirement for developers using the streaming search functionality.

**Tags:** `Data Lineage` `Documentation`
