---
date: 2026-06-07
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Update", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-07  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The tools.list method now supports a toolNames query parameter, allowing developers to filter for specific tools rather than retrieving the entire list.

## Details

A new repeated string parameter, toolNames, has been added to the projects.locations.connections.tools.list method. This allows for more efficient API calls by enabling selective fetching of specific tools by name through a single query.

**Tags:** `Connectors` `API Update` `Filtering`
