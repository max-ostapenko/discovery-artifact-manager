---
date: 2026-06-13
api: connectors.v2
service: Application Integration Connectors
title: "Selective Tool Fetching for Connectors"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective Tool Fetching for Connectors

**Date:** 2026-06-13  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports selective tool fetching via a new toolNames parameter on the tools list method.

## Details

A new repeated query parameter `toolNames` has been added to the `projects.locations.connections.tools.list` method. This allows developers to specify a list of tool names to fetch, enabling more efficient filtering and reducing payload sizes when only specific tools are needed from a connection.

**Tags:** `Connectors` `API Improvement` `Filtering`
