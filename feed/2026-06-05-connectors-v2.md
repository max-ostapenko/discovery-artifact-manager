---
date: 2026-06-05
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Integrations"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-05  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient retrieval of specific integration capabilities.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, meaning developers can pass multiple tool names in a single request to perform selective fetching rather than retrieving the entire toolset for a connection. This is particularly useful for workflows that only require a subset of available tools and want to reduce payload overhead.

**Tags:** `Connectors` `API Optimization` `Integrations`
