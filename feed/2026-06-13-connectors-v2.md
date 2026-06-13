---
date: 2026-06-13
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-13  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool listings by name using a new toolNames query parameter.

## Details

A new repeated string parameter, toolNames, has been added to the projects.locations.connections.tools.list method. This enables selective tool fetching, allowing clients to request only specific tools by name rather than retrieving the entire list associated with a connection, which can help reduce payload sizes and improve client-side efficiency.

**Tags:** `Connectors` `API Improvement` `Filtering`
