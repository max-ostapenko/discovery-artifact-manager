---
date: 2026-06-17
api: connectors.v2
service: Application Integration Connectors
title: "New raw HTTP execution and tool filtering in Connectors v2"
impact: high
breaking: false
tags: ["Integration", "API", "HTTP"]
interesting_score: 8
---

# New raw HTTP execution and tool filtering in Connectors v2

**Date:** 2026-06-17  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method for raw payload delivery and selective tool fetching via a new query parameter.

## Details

The new `executeHttpRequest` method allows developers to send raw byte payloads (supporting REST, GraphQL, XML, SOAP, and Multipart) directly through a connection resource. It includes full support for custom headers and standard HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS). Additionally, the `tools.list` method now supports a `toolNames` repeated query parameter, enabling selective fetching of specific tools rather than retrieving the entire list.

**Tags:** `Integration` `API` `HTTP`
