---
date: 2026-06-14
api: connectors.v2
service: Connectors
title: "Connectors API adds generic HTTP request execution"
impact: high
breaking: false
tags: ["Integration", "HTTP", "API", "Connectors"]
interesting_score: 8
---

# Connectors API adds generic HTTP request execution

**Date:** 2026-06-14  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to send raw HTTP requests through existing connections, supporting any payload format from GraphQL to SOAP.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a flexible way to interact with backends that may not have specific connector actions defined. It supports standard HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and accepts a `rawBody` as bytes, enabling support for REST, GraphQL, XML, SOAP, and Multipart payloads. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective fetching of tool definitions.

**Tags:** `Integration` `HTTP` `API` `Connectors`
