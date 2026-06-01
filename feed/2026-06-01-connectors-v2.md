---
date: 2026-06-01
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["connectors", "api-optimization", "filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-01  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, meaning you can pass multiple specific tool names to retrieve only the definitions you need rather than fetching the entire toolset for a connection.

**Tags:** `connectors` `api-optimization` `filtering`
