---
date: 2026-06-11
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["connectors", "filtering", "api-enhancement"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-11  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter accepts a repeated list of strings, enabling developers to perform selective tool fetching rather than retrieving the entire list of available tools for a connection.

**Tags:** `connectors` `filtering` `api-enhancement`
