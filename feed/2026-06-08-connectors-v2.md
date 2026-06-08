---
date: 2026-06-08
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["connectors", "api-optimization", "filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-08  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now supports filtering tool lists by specific names using a new query parameter.

## Details

A new repeated string parameter, `toolNames`, has been added to the `projects.locations.connections.tools.list` method. This allows developers to perform selective fetching, requesting only the specific tools they need rather than retrieving the entire list and filtering client-side.

**Tags:** `connectors` `api-optimization` `filtering`
