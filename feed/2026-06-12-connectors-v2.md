---
date: 2026-06-12
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching for Connectors"
impact: low
breaking: false
tags: ["API Optimization", "Connectors", "Filtering"]
interesting_score: 4
---

# Selective tool fetching for Connectors

**Date:** 2026-06-12  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now allows developers to filter tool lists by name using a new query parameter.

## Details

A new `toolNames` repeated string parameter has been added to the `projects.locations.connections.tools.list` method. This enables selective fetching of specific tools rather than retrieving the entire list, which is particularly useful for connections with a high volume of defined tools or when building dynamic UIs that only need specific tool metadata.

**Tags:** `API Optimization` `Connectors` `Filtering`
