---
date: 2026-06-01
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "Application Integration", "API Update"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-01  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tool lists by specific names, allowing for more efficient metadata retrieval.

## Details

The `projects.locations.connections.tools.list` method has been updated to include a new `toolNames` query parameter. This is a repeated string field, enabling developers to request metadata for a specific subset of tools rather than fetching the entire list. This is a performance win for integrations managing large toolsets where only a few are needed for a specific execution context.

**Tags:** `Connectors` `Application Integration` `API Update`
