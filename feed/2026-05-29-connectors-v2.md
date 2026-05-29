---
date: 2026-05-29
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-05-29  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports selective tool fetching via a new toolNames parameter in the tools list method.

## Details

Developers can now pass a repeated string parameter `toolNames` to the `projects.locations.connections.tools.list` method. This allows for filtering the returned toolset to only include specific tools by name, reducing payload size and improving client-side processing efficiency when dealing with large tool inventories.

**Tags:** `Connectors` `API Optimization` `Filtering`
