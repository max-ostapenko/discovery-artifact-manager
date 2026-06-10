---
date: 2026-06-10
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Integration", "Connectors", "API Optimization"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-10  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them for a specific connection.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, allowing developers to fetch only the specific tools they need rather than retrieving the entire list for a connection, which is useful for optimizing integration workflows.

**Tags:** `Integration` `Connectors` `API Optimization`
