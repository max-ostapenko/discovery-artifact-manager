---
date: 2026-06-21
api: connectors.v2
service: Integration Connectors
title: "Execute raw HTTP requests via Integration Connectors"
impact: medium
breaking: false
tags: ["Connectors", "Integration", "HTTP", "API-Design"]
interesting_score: 8
---

# Execute raw HTTP requests via Integration Connectors

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new `executeHttpRequest` method enables generic HTTP calls through existing connections, supporting REST, GraphQL, SOAP, and more via raw byte payloads.

## Details

The `connectors.v2` API now includes `executeHttpRequest`, a versatile method for sending arbitrary HTTP requests (GET, POST, PUT, PATCH, DELETE, etc.) through a configured connection. It accepts a `rawBody` as bytes, allowing developers to handle non-JSON formats like XML or Multipart. The response includes the raw body, status code, and headers. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective fetching of tool definitions.

**Tags:** `Connectors` `Integration` `HTTP` `API-Design`
