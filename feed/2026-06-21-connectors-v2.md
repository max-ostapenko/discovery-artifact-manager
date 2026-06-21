---
date: 2026-06-21
api: connectors.v2
service: Integration Connectors
title: "New generic HTTP 'escape hatch' for connections"
impact: high
breaking: false
tags: ["Integrations", "HTTP", "Connectors", "API-Design"]
interesting_score: 8
---

# New generic HTTP 'escape hatch' for connections

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to send arbitrary HTTP requests through a connection, supporting REST, GraphQL, XML, and SOAP via raw byte payloads.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a generic interface for interacting with backend services. Instead of relying on pre-defined connector actions, developers can now specify the `url`, `httpMethod` (GET, POST, PUT, etc.), `headers`, and a `rawBody` as bytes. This effectively turns the connector into a flexible HTTP proxy. Additionally, the `tools.list` method now includes a `toolNames` query parameter, allowing for selective fetching of specific tools rather than retrieving the entire list.

**Tags:** `Integrations` `HTTP` `Connectors` `API-Design`
