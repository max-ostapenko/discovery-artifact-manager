---
date: 2026-06-06
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-06  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name during list operations, allowing for more efficient metadata retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter is a repeated string, enabling developers to fetch only specific tools by name rather than retrieving the entire set. This is particularly useful for integrations managing large toolsets where selective fetching reduces payload size and processing overhead.

**Tags:** `Connectors` `API Improvement` `Filtering`
