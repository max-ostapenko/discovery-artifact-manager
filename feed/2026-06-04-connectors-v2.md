---
date: 2026-06-04
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Update", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-04  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient and targeted tool discovery.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, meaning you can pass multiple specific tool names to retrieve only those definitions rather than fetching the entire list of available tools for a connection.

**Tags:** `Connectors` `API Update` `Filtering`
