---
date: 2026-06-12
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["connectors", "filtering", "api-update"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-12  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports selective tool fetching via a new toolNames parameter on the tools list method.

## Details

A new repeated query parameter toolNames has been added to projects.locations.connections.tools.list. This allows developers to request specific tools by name rather than fetching the entire list, which is particularly useful for connections with a large number of defined tools or when optimizing client-side performance.

**Tags:** `connectors` `filtering` `api-update`
