---
date: 2026-06-04
api: connectors.v2
service: Application Integration Connectors
title: "Selective Tool Fetching in Connectors API"
impact: low
breaking: false
tags: ["API Enhancement", "Filtering", "Connectors"]
interesting_score: 4
---

# Selective Tool Fetching in Connectors API

**Date:** 2026-06-04  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now supports filtering tools by name when listing them, allowing for more efficient data retrieval.

## Details

A new `toolNames` query parameter has been added to the `projects.locations.connections.tools.list` method. This parameter accepts a repeated list of strings, enabling developers to perform selective tool fetching rather than retrieving the entire list of available tools for a connection.

**Tags:** `API Enhancement` `Filtering` `Connectors`
