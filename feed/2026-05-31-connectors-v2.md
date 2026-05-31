---
date: 2026-05-31
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Update", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-05-31  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter is a repeated string, allowing developers to pass multiple specific tool names to fetch only the metadata for those tools instead of the full set. This is particularly useful for reducing payload sizes when working with connections that expose a large number of tools.

**Tags:** `Connectors` `API Update` `Filtering`
