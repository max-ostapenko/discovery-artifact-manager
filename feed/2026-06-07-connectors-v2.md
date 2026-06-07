---
date: 2026-06-07
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-07  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool lists by specific names using a new query parameter.

## Details

A new `toolNames` repeated string parameter has been added to the `projects.locations.connections.tools.list` method. This enables selective fetching, allowing you to request only the specific tools you need rather than retrieving the entire set for a connection, which should help reduce payload sizes and improve client-side efficiency.

**Tags:** `Connectors` `API Improvement` `Filtering`
