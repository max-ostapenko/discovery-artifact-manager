---
date: 2026-06-09
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Filtering", "Application Integration"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-09  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them for a specific connection.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter accepts a repeated list of strings, allowing developers to perform selective tool fetching rather than retrieving the entire toolset for a connection. This is particularly useful for optimizing client-side performance when only a subset of tools is required for a specific integration task.

**Tags:** `Connectors` `API Filtering` `Application Integration`
