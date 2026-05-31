---
date: 2026-05-31
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-05-31  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient retrieval of specific tool definitions.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, enabling developers to request a specific subset of tools by name rather than fetching the entire list for a connection. This is particularly useful for reducing latency and payload size when dealing with connections that expose a large number of tools.

**Tags:** `Connectors` `API Improvement` `Filtering`
