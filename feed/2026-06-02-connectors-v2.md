---
date: 2026-06-02
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-02  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool lists by specific names using a new query parameter.

## Details

A new `toolNames` repeated string parameter has been added to the `projects.locations.connections.tools.list` method. This enables selective tool fetching, allowing clients to request only the specific tools they need rather than retrieving the entire list for a connection, which should improve performance for connections with many tools.

**Tags:** `Connectors` `API Improvement` `Filtering`
