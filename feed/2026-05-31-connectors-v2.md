---
date: 2026-05-31
api: connectors.v2
service: Application Integration Connectors
title: "Selective tool fetching via toolNames parameter"
impact: low
breaking: false
tags: ["Connectors", "API Update", "Filtering"]
interesting_score: 4
---

# Selective tool fetching via toolNames parameter

**Date:** 2026-05-31  
**API:** `connectors.v2`  
**Impact:** Low  

## Summary

The Connectors API now allows developers to filter tool lists by specific names using a new toolNames query parameter.

## Details

The projects.locations.connections.tools.list method has been updated to include a toolNames parameter. This is a repeated string field, meaning you can pass multiple names in a single request to retrieve only the specific tools required for your integration logic, reducing unnecessary data transfer.

**Tags:** `Connectors` `API Update` `Filtering`
