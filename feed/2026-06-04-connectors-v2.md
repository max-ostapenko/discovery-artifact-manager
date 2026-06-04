---
date: 2026-06-04
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching via toolNames parameter"
impact: low
breaking: false
tags: ["Connectors", "API Design", "Optimization"]
interesting_score: 4
---

# Selective tool fetching via toolNames parameter

**Date:** 2026-06-04  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tool lists by specific names, allowing for more efficient metadata retrieval.

## Details

A new repeated string parameter, `toolNames`, has been added to the `projects.locations.connections.tools.list` method. This allows developers to perform selective tool fetching by passing a list of specific tool names in the query string, reducing the payload size and processing time when only a subset of tools is required.

**Tags:** `Connectors` `API Design` `Optimization`
