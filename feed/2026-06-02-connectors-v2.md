---
date: 2026-06-02
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-02  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool listings by specific names, enabling more efficient retrieval of tool metadata.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, allowing developers to request a specific subset of tools rather than fetching the entire list, which is particularly useful for integrations with large toolsets.

**Tags:** `Connectors` `API Optimization` `Filtering`
