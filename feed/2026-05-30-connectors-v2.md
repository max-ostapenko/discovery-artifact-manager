---
date: 2026-05-30
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-05-30  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tools by name when listing them, allowing for more efficient retrieval of specific tool definitions.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, allowing developers to pass multiple specific tool names to retrieve only the metadata for those tools rather than fetching the entire list and filtering client-side.

**Tags:** `Connectors` `API Improvement` `Filtering`
