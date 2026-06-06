---
date: 2026-06-06
api: connectors.v2
service: Application Integration Connectors
title: "Selective Tool Fetching in Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Update", "Filtering"]
interesting_score: 4
---

# Selective Tool Fetching in Connectors API

**Date:** 2026-06-06  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tools by name when listing them, enabling more efficient and targeted resource retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string field, allowing developers to request a specific subset of tools by name rather than fetching the entire list for a connection.

**Tags:** `Connectors` `API Update` `Filtering`
