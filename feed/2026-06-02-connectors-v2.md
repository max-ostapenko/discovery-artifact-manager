---
date: 2026-06-02
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Design", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-02  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tool lists by specific names using the new toolNames query parameter.

## Details

A new toolNames parameter has been added to the projects.locations.connections.tools.list method. This allows developers to pass a repeated list of strings to fetch only specific tools rather than retrieving the entire set, which is particularly useful for optimizing performance when dealing with connections that expose many tools.

**Tags:** `Connectors` `API Design` `Filtering`
