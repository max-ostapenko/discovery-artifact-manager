---
date: 2026-06-08
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Performance"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-08  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tool lists by specific names via a new query parameter.

## Details

A new `toolNames` repeated query parameter has been added to the `projects.locations.connections.tools.list` method. This allows developers to perform selective fetching, retrieving only the specific tools required for their integration rather than the entire set.

**Tags:** `Connectors` `API Improvement` `Performance`
