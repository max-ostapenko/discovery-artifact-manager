---
date: 2026-06-20
api: connectors.v2
service: App Integration Connectors
title: "New raw HTTP execution and selective tool fetching"
impact: high
breaking: false
tags: ["integration", "http", "extensibility"]
interesting_score: 8
---

# New raw HTTP execution and selective tool fetching

**Date:** 2026-06-20  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Connectors v2 now supports a universal 'escape hatch' with the executeHttpRequest method, allowing raw HTTP calls through existing connections.

## Details

The major addition is the `executeHttpRequest` method on the connection resource. This method allows developers to send arbitrary HTTP requests (GET, POST, PUT, PATCH, DELETE, etc.) with custom headers and raw byte payloads, making it possible to support GraphQL, SOAP, and XML even if the specific connector doesn't have a pre-defined schema for them. Additionally, the `tools.list` method now includes a `toolNames` query parameter, enabling selective fetching of specific tools rather than retrieving the entire list.

**Tags:** `integration` `http` `extensibility`
