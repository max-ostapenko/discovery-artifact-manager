---
date: 2026-06-05
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching added to Connectors API"
impact: low
breaking: false
tags: ["Connectors", "API Improvement", "Filtering"]
interesting_score: 4
---

# Selective tool fetching added to Connectors API

**Date:** 2026-06-05  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors v2 API now allows developers to filter tool lists by specific names using the new toolNames query parameter.

## Details

A new toolNames parameter has been added to the projects.locations.connections.tools.list method. This is a repeated string query parameter, allowing developers to pass multiple specific names to selectively fetch only the tools required for their integration logic, rather than retrieving the entire set associated with a connection.

**Tags:** `Connectors` `API Improvement` `Filtering`
