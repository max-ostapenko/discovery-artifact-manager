---
date: 2026-06-08
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Integration", "Connectors", "API Design"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-08  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them for a specific connection.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter is a repeated string, allowing developers to fetch a specific subset of tools rather than retrieving the entire list. This is a useful optimization for connections that define a large number of tools.

**Tags:** `Integration` `Connectors` `API Design`
