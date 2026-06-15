---
date: 2026-06-15
api: connectors.v2
service: App Integration Connectors
title: "New generic HTTP execution for all connections"
impact: medium
breaking: false
tags: ["http", "passthrough", "integration"]
interesting_score: 8
---

# New generic HTTP execution for all connections

**Date:** 2026-06-15  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method, allowing developers to bypass specific connector schemas and send raw HTTP requests through established connections.

## Details

The new `executeHttpRequest` method on the `connections` resource enables raw byte payloads, supporting REST/JSON, GraphQL, XML, SOAP, and Multipart formats. It accepts a standard set of HTTP methods (GET, POST, PUT, PATCH, DELETE, etc.), custom headers, and a fully resolved URL. Additionally, the `tools.list` method now includes a `toolNames` query parameter, allowing for selective fetching of specific tools rather than the entire list.

**Tags:** `http` `passthrough` `integration`
