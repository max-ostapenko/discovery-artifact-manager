---
date: 2026-06-03
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["API Optimization", "Connectors", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-03  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports selective tool fetching via a new toolNames parameter in the tools list method.

## Details

A new toolNames repeated string parameter has been added to the projects.locations.connections.tools.list method. This allows developers to pass a list of specific tool names in the query string to filter the response, enabling more efficient data retrieval when only a subset of tools is required.

**Tags:** `API Optimization` `Connectors` `Filtering`
