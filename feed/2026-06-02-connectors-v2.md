---
date: 2026-06-02
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Update", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-02  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name during list operations, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter accepts a repeated list of strings, enabling developers to fetch only specific tools rather than the entire collection. This is particularly useful for reducing payload sizes and improving performance when working with connections that expose many tools.

**Tags:** `Connectors` `API Update` `Filtering`
