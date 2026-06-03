---
date: 2026-06-03
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Update", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-03  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter is a repeated string, enabling developers to specify a list of tool names to fetch selectively rather than retrieving the entire set of tools associated with a connection.

**Tags:** `Connectors` `API Update` `Filtering`
