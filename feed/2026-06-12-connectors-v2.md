---
date: 2026-06-12
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Integration"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-12  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them on a connection, allowing for more efficient retrieval of specific tool definitions.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter is a repeated string, enabling developers to perform selective tool fetching rather than retrieving the entire toolset for a given connection. This is particularly useful for reducing payload sizes in integration workflows or LLM tool-calling scenarios.

**Tags:** `Connectors` `API Optimization` `Integration`
