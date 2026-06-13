---
date: 2026-06-13
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-13  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient retrieval of specific tool configurations.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter is a repeated string, allowing developers to pass multiple specific tool names to fetch a targeted subset of tools rather than retrieving the entire list and filtering client-side.

**Tags:** `Connectors` `API Improvement` `Filtering`
