---
date: 2026-06-15
api: connectors.v2
service: Application Integration Connectors
title: "Generic HTTP execution comes to Connectors V2"
impact: medium
breaking: false
tags: ["integration", "connectors", "http"]
interesting_score: 8
---

# Generic HTTP execution comes to Connectors V2

**Date:** 2026-06-15  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows developers to send raw HTTP requests—including REST, GraphQL, and SOAP—directly through an established connection.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a flexible escape hatch for interacting with backends. It supports standard verbs (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and handles payloads as raw bytes via the `rawBody` field, making it compatible with any format from JSON to Multipart. The response includes the raw body, headers, and status codes. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective tool fetching.

**Tags:** `integration` `connectors` `http`
