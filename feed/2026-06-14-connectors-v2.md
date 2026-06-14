---
date: 2026-06-14
api: connectors.v2
service: Application Integration Connectors
title: "New generic HTTP execution and tool filtering"
impact: medium
breaking: false
tags: ["Connectors", "Integration", "HTTP"]
interesting_score: 7
---

# New generic HTTP execution and tool filtering

**Date:** 2026-06-14  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

Connectors v2 now supports executing raw HTTP requests through connections and adds selective tool fetching.

## Details

A major new method, `executeHttpRequest`, has been added to the connections resource. This allows developers to send arbitrary HTTP requests (GET, POST, PUT, PATCH, DELETE, etc.) with raw byte payloads, effectively supporting any format including REST, GraphQL, XML, and SOAP. The request schema includes `url`, `httpMethod`, `headers`, and `rawBody`, while the response provides the `statusCode`, `reason`, and raw `body`. Additionally, the `tools.list` method now accepts a `toolNames` parameter for selective fetching.

**Tags:** `Connectors` `Integration` `HTTP`
