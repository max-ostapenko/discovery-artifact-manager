---
date: 2026-06-10
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-10  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The tools.list method now supports a toolNames query parameter, allowing developers to filter for specific tools rather than retrieving the entire list.

## Details

A new repeated string parameter `toolNames` has been added to the `projects.locations.connections.tools.list` method. This enables selective fetching, which is particularly useful when dealing with connections that expose a large number of tools, helping to reduce payload size and client-side filtering logic.

**Tags:** `Connectors` `API Improvement` `Filtering`
