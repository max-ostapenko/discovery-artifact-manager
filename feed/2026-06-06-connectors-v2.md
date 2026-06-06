---
date: 2026-06-06
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["API Improvement", "Performance", "Connectors"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-06  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool listings by specific names using a new query parameter.

## Details

A new `toolNames` repeated string parameter has been added to the `projects.locations.connections.tools.list` method. This enables selective tool fetching, allowing you to retrieve metadata for a specific subset of tools rather than the entire list, which is particularly useful for connections with a large number of available tools.

**Tags:** `API Improvement` `Performance` `Connectors`
