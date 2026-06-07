---
date: 2026-06-07
api: connectors.v2
service: Application Integration Connectors
title: "Selective Tool Fetching for Connectors"
impact: low
breaking: false
tags: ["integration", "connectors", "api-optimization"]
interesting_score: 4
---

# Selective Tool Fetching for Connectors

**Date:** 2026-06-07  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new toolNames query parameter has been added to the projects.locations.connections.tools.list method. This is a repeated string parameter, enabling developers to fetch only specific tools associated with a connection rather than retrieving the entire list, which is particularly useful for connections with a large number of defined tools.

**Tags:** `integration` `connectors` `api-optimization`
