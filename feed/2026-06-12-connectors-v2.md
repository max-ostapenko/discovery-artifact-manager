---
date: 2026-06-12
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Update", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-12  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name during list operations, allowing for more efficient retrieval of specific tool definitions.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter accepts a repeated list of strings, enabling developers to fetch only the specific tool metadata they require rather than retrieving the entire toolset for a connection.

**Tags:** `Connectors` `API Update` `Filtering`
