---
date: 2026-06-19
api: connectors.v2
service: Application Integration Connectors
title: "Connectors v2 adds generic HTTP request execution"
impact: high
breaking: false
tags: ["Integration", "Connectors", "HTTP", "API"]
interesting_score: 8
---

# Connectors v2 adds generic HTTP request execution

**Date:** 2026-06-19  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to send arbitrary HTTP requests through a connection, supporting any payload format via raw bytes.

## Details

The API now includes the `executeHttpRequest` method on connection resources, effectively providing a 'universal' action for integrations. This method supports standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and accepts a `rawBody` byte field, enabling support for REST/JSON, GraphQL, XML, SOAP, and Multipart payloads. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective fetching of tool definitions.

**Tags:** `Integration` `Connectors` `HTTP` `API`
