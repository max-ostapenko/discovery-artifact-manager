---
date: 2026-06-21
api: connectors.v2
service: Application Integration Connectors
title: "Generic HTTP request execution added to Connectors v2"
impact: high
breaking: false
tags: ["Connectors", "Integration", "HTTP", "GraphQL"]
interesting_score: 8
---

# Generic HTTP request execution added to Connectors v2

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method, enabling raw HTTP calls (REST, GraphQL, SOAP) directly through existing connections.

## Details

The new `executeHttpRequest` method allows developers to bypass specific connector schemas by sending raw byte payloads via the `rawBody` field. It supports standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and custom headers. This is a powerful escape hatch for interacting with legacy SOAP services, GraphQL endpoints, or multipart payloads that don't fit into standard connector schemas. Additionally, the `tools.list` method gained a `toolNames` query parameter for selective tool fetching.

**Tags:** `Connectors` `Integration` `HTTP` `GraphQL`
