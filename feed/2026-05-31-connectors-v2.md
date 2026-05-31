---
date: 2026-05-31
api: connectors.v2
service: Connectors
title: "Selective Tool Fetching for Connectors"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Tools"]
interesting_score: 4
---

# Selective Tool Fetching for Connectors

**Date:** 2026-05-31  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tools by name when listing them, allowing for more efficient retrieval of specific tool definitions.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, enabling developers to fetch a specific subset of tools by name rather than retrieving the entire list and filtering client-side.

**Tags:** `Connectors` `API Optimization` `Tools`
