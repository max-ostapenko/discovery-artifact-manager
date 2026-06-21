---
date: 2026-06-21
api: connectors.v2
service: Application Integration Connectors
title: "Generic HTTP 'Escape Hatch' added to Connectors v2"
impact: high
breaking: false
tags: ["Integrations", "HTTP", "Networking"]
interesting_score: 8
---

# Generic HTTP 'Escape Hatch' added to Connectors v2

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows sending raw HTTP requests through existing connections, supporting REST, GraphQL, SOAP, and more.

## Details

Developers can now use projects.locations.connections.executeHttpRequest to send arbitrary payloads. The request schema accepts a rawBody (bytes), url, and httpMethod, while the response returns the raw body, statusCode, and headers. This effectively provides a generic proxy for any HTTP-based service, bypassing the need for specific connector schemas when handling complex formats like XML or Multipart. Additionally, the connections.tools.list method now supports a toolNames query parameter for selective tool fetching.

**Tags:** `Integrations` `HTTP` `Networking`
