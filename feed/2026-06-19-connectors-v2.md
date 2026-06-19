---
date: 2026-06-19
api: connectors.v2
service: Integration Connectors
title: "Raw HTTP Request Support for Connections"
impact: medium
breaking: false
tags: ["Integration Connectors", "API", "HTTP"]
interesting_score: 7
---

# Raw HTTP Request Support for Connections

**Date:** 2026-06-19  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows executing arbitrary HTTP requests through existing connections, supporting any payload format via raw bytes.

## Details

Developers can now use projects.locations.connections.executeHttpRequest to send custom REST, GraphQL, XML, or SOAP requests. The method accepts an ExecuteHttpRequestRequest object containing the target URL, HTTP method (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS), headers, and a rawBody as bytes. The response provides the status code, reason phrase, headers, and the raw response body. Additionally, the tools.list method now supports a toolNames query parameter for selective tool fetching.

**Tags:** `Integration Connectors` `API` `HTTP`
