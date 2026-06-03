---
date: 2026-06-03
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-03  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter accepts a repeated list of strings, enabling developers to fetch only the specific tools they need rather than retrieving the entire set for a given connection. This is particularly useful for reducing payload overhead in environments with many registered tools.

**Tags:** `Connectors` `API Improvement` `Filtering`
