---
date: 2026-06-05
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["connectors", "api-updates", "filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-05  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tools by name when listing them, allowing for more efficient retrieval of specific resources.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, meaning you can pass multiple specific tool names to fetch only the relevant metadata rather than retrieving the entire list of available tools.

**Tags:** `connectors` `api-updates` `filtering`
