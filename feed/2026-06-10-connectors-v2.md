---
date: 2026-06-10
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-10  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name during list operations, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, enabling developers to fetch a specific subset of tools rather than the entire collection, which is particularly useful for reducing payload size in complex integrations.

**Tags:** `Connectors` `API` `Filtering`
