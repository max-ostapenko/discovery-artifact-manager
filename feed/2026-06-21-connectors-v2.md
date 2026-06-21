---
date: 2026-06-21
api: connectors.v2
service: Application Integration Connectors
title: "New executeHttpRequest method for generic API calls"
impact: high
breaking: false
tags: ["Connectors", "HTTP", "Integration", "API"]
interesting_score: 8
---

# New executeHttpRequest method for generic API calls

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Connectors v2 now supports executing arbitrary HTTP requests through existing connections, enabling support for GraphQL, SOAP, and custom payloads.

## Details

The new `executeHttpRequest` method allows developers to bypass specific connector schemas and send raw byte payloads (`rawBody`) to a target `url` using standard HTTP methods (GET, POST, PUT, PATCH, DELETE, etc.). This acts as a powerful escape hatch for interacting with endpoints that require XML, Multipart, or GraphQL which might not be natively modeled in a specific connector. Additionally, the `tools.list` method now accepts a `toolNames` query parameter for selective resource fetching, improving performance when only specific tools are needed.

**Tags:** `Connectors` `HTTP` `Integration` `API`
