---
date: 2026-06-14
api: connectors.v2
service: Application Integration Connectors
title: "Generic HTTP escape hatch added to Connectors v2"
impact: high
breaking: false
tags: ["Integration", "Connectors", "HTTP", "API"]
interesting_score: 8
---

# Generic HTTP escape hatch added to Connectors v2

**Date:** 2026-06-14  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to send raw HTTP requests through a connection, bypassing specific connector schemas for REST, GraphQL, or SOAP.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a generic interface for interacting with backends. It supports standard HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and accepts a `rawBody` as bytes, enabling support for any payload format including XML and Multipart. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective fetching of specific tools.

**Tags:** `Integration` `Connectors` `HTTP` `API`
