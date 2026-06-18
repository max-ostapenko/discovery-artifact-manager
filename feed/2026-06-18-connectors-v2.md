---
date: 2026-06-18
api: connectors.v2
service: Application Integration Connectors
title: "Connectors V2 adds raw HTTP 'escape hatch' method"
impact: high
breaking: false
tags: ["Integration", "Connectors", "HTTP", "GraphQL"]
interesting_score: 8
---

# Connectors V2 adds raw HTTP 'escape hatch' method

**Date:** 2026-06-18  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to bypass connector-specific schemas and send raw HTTP requests, supporting GraphQL, SOAP, and custom XML.

## Details

The major addition is the `executeHttpRequest` method on the `connections` resource. This method acts as a universal proxy, allowing you to pass a `rawBody` (as bytes), custom `headers`, and a target `url` using standard HTTP methods (GET, POST, etc.). This is particularly useful for interacting with legacy SOAP services or modern GraphQL endpoints that aren't fully modeled by a specific connector. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective fetching of tool definitions.

**Tags:** `Integration` `Connectors` `HTTP` `GraphQL`
