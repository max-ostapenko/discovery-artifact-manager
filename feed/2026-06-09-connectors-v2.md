---
date: 2026-06-09
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-09  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool listings by specific names using a new query parameter.

## Details

A new `toolNames` repeated string parameter has been added to the `projects.locations.connections.tools.list` method. This enables selective fetching, allowing you to retrieve only the specific tools required for your integration rather than the entire list, which can improve performance and reduce payload sizes.

**Tags:** `Connectors` `API Optimization` `Filtering`
