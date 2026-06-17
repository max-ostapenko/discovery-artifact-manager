---
date: 2026-06-17
api: connectors.v2
service: Application Integration Connectors
title: "New generic HTTP 'escape hatch' for connections"
impact: medium
breaking: false
tags: ["Connectors", "Integration", "HTTP"]
interesting_score: 7
---

# New generic HTTP 'escape hatch' for connections

**Date:** 2026-06-17  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows developers to send raw HTTP requests through existing connections, bypassing specific connector schemas for custom payloads.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a generic way to interact with backends using REST, GraphQL, XML, SOAP, or Multipart formats by passing raw bytes. The method accepts a `rawBody`, `url`, and `httpMethod`, returning the full response including status codes and headers. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective tool fetching.

**Tags:** `Connectors` `Integration` `HTTP`
