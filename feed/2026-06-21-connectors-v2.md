---
date: 2026-06-21
api: connectors.v2
service: Application Integration Connectors
title: "Generic HTTP execution comes to Connectors v2"
impact: medium
breaking: false
tags: ["Integration", "HTTP", "API"]
interesting_score: 7
---

# Generic HTTP execution comes to Connectors v2

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method, allowing raw HTTP calls through existing connections for any payload format.

## Details

The new `executeHttpRequest` method enables developers to send raw bytes to a target URL using standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, etc.). This bypasses the need for pre-defined schemas, supporting GraphQL, SOAP, and Multipart payloads directly. Additionally, the `tools.list` method has been updated with a `toolNames` query parameter, allowing for selective fetching of specific tools rather than retrieving the entire list.

**Tags:** `Integration` `HTTP` `API`
