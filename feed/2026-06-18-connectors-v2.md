---
date: 2026-06-18
api: connectors.v2
service: Application Integration Connectors
title: "Connectors v2 adds raw HTTP execution escape hatch"
impact: high
breaking: false
tags: ["Integration", "Connectors", "HTTP", "REST"]
interesting_score: 8
---

# Connectors v2 adds raw HTTP execution escape hatch

**Date:** 2026-06-18  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Integration Connectors now supports a generic executeHttpRequest method, allowing developers to send raw payloads (JSON, XML, GraphQL, SOAP) directly to backends.

## Details

The new `executeHttpRequest` method on the `connections` resource provides a universal way to interact with backend systems. It supports standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and uses a `rawBody` byte field to handle any payload format. This effectively acts as an escape hatch for when a connector's predefined actions or entities don't cover a specific use case. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective tool fetching.

**Tags:** `Integration` `Connectors` `HTTP` `REST`
