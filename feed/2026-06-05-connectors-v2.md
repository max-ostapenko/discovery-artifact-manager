---
date: 2026-06-05
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["integration", "connectors", "api-filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-05  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient retrieval of specific tool definitions.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter is a repeated string, enabling developers to fetch a specific subset of tools by name rather than retrieving the entire list associated with a connection.

**Tags:** `integration` `connectors` `api-filtering`
