---
date: 2026-06-04
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["connectors", "filtering", "api-update"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-04  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new toolNames query parameter has been added to the projects.locations.connections.tools.list method. This parameter accepts a repeated list of strings, enabling developers to perform selective tool fetching instead of retrieving the entire toolset for a connection. This is particularly useful for reducing payload sizes and improving performance when working with complex connector configurations.

**Tags:** `connectors` `filtering` `api-update`
