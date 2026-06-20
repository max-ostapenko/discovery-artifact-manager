---
date: 2026-06-20
api: connectors.v2
service: Application Integration Connectors
title: "Raw HTTP execution comes to Integration Connectors"
impact: medium
breaking: false
tags: ["Integration", "Connectors", "HTTP"]
interesting_score: 7
---

# Raw HTTP execution comes to Integration Connectors

**Date:** 2026-06-20  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows for generic HTTP requests through existing connections, supporting any payload format from REST to SOAP.

## Details

The addition of `executeHttpRequest` on connection resources allows developers to bypass specific connector schemas and perform raw HTTP calls. The method accepts a `rawBody` (bytes), `headers`, and a target `url`, supporting standard methods like GET, POST, PUT, PATCH, and DELETE. This is particularly useful for interacting with endpoints or payload formats (like GraphQL or SOAP) not explicitly modeled by a connector. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective fetching of tool definitions.

**Tags:** `Integration` `Connectors` `HTTP`
