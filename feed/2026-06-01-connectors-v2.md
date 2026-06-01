---
date: 2026-06-01
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching via toolNames parameter"
impact: low
breaking: false
tags: ["Connectors", "Application Integration", "API Improvement"]
interesting_score: 4
---

# Selective tool fetching via toolNames parameter

**Date:** 2026-06-01  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tools by name when listing them on a connection, allowing for more efficient retrieval of specific tool definitions.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, enabling developers to pass multiple tool names to selectively fetch only the tools they need. This is particularly useful for GenAI and orchestration workflows where you may want to limit the tool definitions retrieved from a specific connector instance.

**Tags:** `Connectors` `Application Integration` `API Improvement`
