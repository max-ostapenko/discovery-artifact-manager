---
date: 2026-06-09
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-09  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool listings by specific names using the new toolNames query parameter.

## Details

A new toolNames repeated string parameter has been added to the projects.locations.connections.tools.list method. This enables selective fetching of tools, allowing clients to request metadata for a specific subset of tools rather than retrieving the entire list for a connection, which is particularly useful for large connector configurations.

**Tags:** `Connectors` `API Improvement` `Filtering`
