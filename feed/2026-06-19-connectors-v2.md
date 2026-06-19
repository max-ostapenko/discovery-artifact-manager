---
date: 2026-06-19
api: connectors.v2
service: Application Integration Connectors
title: "New executeHttpRequest method for raw HTTP calls"
impact: high
breaking: false
tags: ["Integration", "Connectors", "HTTP", "API-Design"]
interesting_score: 8
---

# New executeHttpRequest method for raw HTTP calls

**Date:** 2026-06-19  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Connectors v2 now supports executing generic HTTP requests directly through a connection, providing a flexible escape hatch for unsupported payload formats or custom endpoints.

## Details

The new `executeHttpRequest` method on the connection resource allows for raw byte payloads, supporting REST, GraphQL, XML, and SOAP. It includes full control over HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and headers via the `ExecuteHttpRequestRequest` schema. This effectively allows developers to use the connector's authentication and networking context for arbitrary HTTP calls. Additionally, the `tools.list` method gained a `toolNames` query parameter for selective tool retrieval.

**Tags:** `Integration` `Connectors` `HTTP` `API-Design`
