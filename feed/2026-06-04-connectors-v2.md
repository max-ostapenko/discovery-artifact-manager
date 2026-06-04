---
date: 2026-06-04
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Performance"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-04  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tool listings by specific names, allowing for more efficient metadata retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This is a repeated string parameter, meaning developers can now pass multiple specific tool names to the list request to perform selective fetching rather than retrieving the entire toolset for a connection.

**Tags:** `Connectors` `API Improvement` `Performance`
