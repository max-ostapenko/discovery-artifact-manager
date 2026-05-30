---
date: 2026-05-30
api: connectors.v2
service: App Integration Connectors
title: "Selective Tool Fetching for Connectors"
impact: low
breaking: false
tags: ["Connectors", "API", "Filtering"]
interesting_score: 4
---

# Selective Tool Fetching for Connectors

**Date:** 2026-05-30  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tools by name when listing them, enabling more efficient retrieval for specific integrations.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, allowing developers to pass a list of specific tool names to fetch rather than retrieving the entire toolset associated with a connection. This is particularly useful for reducing payload sizes in complex integration workflows.

**Tags:** `Connectors` `API` `Filtering`
