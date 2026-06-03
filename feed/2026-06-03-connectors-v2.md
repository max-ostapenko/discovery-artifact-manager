---
date: 2026-06-03
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Optimization", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-03  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool lists by specific names using a new query parameter.

## Details

A new `toolNames` repeated string parameter has been added to the `projects.locations.connections.tools.list` method. This enables selective tool fetching, allowing clients to request only the specific tools they need rather than retrieving the full set of tools associated with a connection. This is particularly useful for reducing payload sizes when working with connections that expose a large number of tools.

**Tags:** `Connectors` `API Optimization` `Filtering`
