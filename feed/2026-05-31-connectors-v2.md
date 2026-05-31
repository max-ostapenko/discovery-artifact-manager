---
date: 2026-05-31
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["connectors", "filtering", "performance"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-05-31  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name during list operations, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, meaning you can pass multiple specific tool names to fetch only the resources you need rather than retrieving the entire toolset for a connection.

**Tags:** `connectors` `filtering` `performance`
