---
date: 2026-06-10
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "Application Integration", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-10  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient resource retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter accepts a repeated list of strings, enabling developers to perform selective tool fetching rather than retrieving the entire toolset for a connection. This is particularly useful for integrations that only require a subset of available tools and want to reduce payload sizes.

**Tags:** `Connectors` `Application Integration` `Filtering`
