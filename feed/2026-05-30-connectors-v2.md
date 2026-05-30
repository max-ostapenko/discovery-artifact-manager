---
date: 2026-05-30
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["connectors", "api-optimization", "filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-05-30  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient discovery and reduced payloads.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter is a repeated string field, meaning developers can pass multiple specific tool names in a single request to perform selective fetching rather than retrieving the entire toolset for a connection.

**Tags:** `connectors` `api-optimization` `filtering`
