---
date: 2026-06-03
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors v2"
impact: low
breaking: false
tags: ["Integrations", "Connectors", "API Design"]
interesting_score: 4
---

# Selective tool fetching added to Connectors v2

**Date:** 2026-06-03  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The list method for connection tools now supports a toolNames filter, allowing developers to fetch specific tools by name.

## Details

A new repeated query parameter `toolNames` has been added to the `projects.locations.connections.tools.list` method. This allows for selective tool fetching, which is particularly useful for optimizing performance when a connection exposes a large number of tools but only a specific subset is required for a task.

**Tags:** `Integrations` `Connectors` `API Design`
