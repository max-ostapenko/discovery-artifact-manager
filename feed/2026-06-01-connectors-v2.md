---
date: 2026-06-01
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-01  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new repeated query parameter 'toolNames' has been added to the 'projects.locations.connections.tools.list' method. This allows developers to specify a list of specific tool names to fetch selectively, which is a significant improvement over fetching the entire toolset and filtering client-side.

**Tags:** `Connectors` `API Optimization` `Filtering`
