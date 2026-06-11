---
date: 2026-06-11
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "Integrations", "API Design"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-11  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The tools.list method now supports a toolNames query parameter, allowing developers to fetch specific tools by name rather than retrieving the entire list.

## Details

A new repeated string parameter `toolNames` has been added to the `projects.locations.connections.tools.list` method. This enables selective tool fetching, which is particularly useful for optimizing workflows where only a subset of available tools is needed for a specific execution context or LLM prompt, reducing the payload size and client-side processing.

**Tags:** `Connectors` `Integrations` `API Design`
