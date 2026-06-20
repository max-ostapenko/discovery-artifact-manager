---
date: 2026-06-20
api: connectors.v2
service: Application Integration Connectors
title: "New raw HTTP execution support for Connectors"
impact: high
breaking: false
tags: ["Connectors", "Integration", "HTTP"]
interesting_score: 8
---

# New raw HTTP execution support for Connectors

**Date:** 2026-06-20  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method, allowing developers to bypass standard connector schemas and perform raw HTTP calls through established connections.

## Details

The new `executeHttpRequest` method enables support for any payload format—including REST/JSON, GraphQL, XML, SOAP, and Multipart—by passing the rendered payload as raw bytes. The request schema (`ExecuteHttpRequestRequest`) accepts a `url`, `httpMethod`, `headers`, and a `rawBody` byte field. The response includes the status code, reason phrase, and raw body. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective tool fetching.

**Tags:** `Connectors` `Integration` `HTTP`
