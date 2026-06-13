---
date: 2026-06-13
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Integrations", "Connectors", "Performance"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-13  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The tools.list method now supports a toolNames query parameter, allowing developers to filter for specific tools within a connection.

## Details

A new repeated string parameter `toolNames` has been added to the `projects.locations.connections.tools.list` method. This allows for 'selective tool fetching,' enabling developers to request only a specific subset of tools by name rather than retrieving the entire list, which improves efficiency for large connector configurations.

**Tags:** `Integrations` `Connectors` `Performance`
