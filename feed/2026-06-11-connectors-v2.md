---
date: 2026-06-11
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Integration"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-11  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool listings by specific names using a new query parameter.

## Details

A new `toolNames` repeated string parameter has been added to the `projects.locations.connections.tools.list` method. This allows for selective tool fetching, enabling clients to request only the specific tools they need rather than retrieving the entire list for a given connection, which can improve performance and reduce payload overhead.

**Tags:** `Connectors` `API Optimization` `Integration`
