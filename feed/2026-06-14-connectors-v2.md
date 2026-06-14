---
date: 2026-06-14
api: connectors.v2
service: Application Integration Connectors
title: "New raw HTTP execution for all connections"
impact: high
breaking: false
tags: ["http", "proxy", "integration"]
interesting_score: 8
---

# New raw HTTP execution for all connections

**Date:** 2026-06-14  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method, allowing developers to send arbitrary HTTP requests through existing connection contexts.

## Details

The new `executeHttpRequest` method on the Connection resource enables support for any payload format (REST/JSON, GraphQL, XML, SOAP, Multipart) by passing raw bytes in the `rawBody` field. It supports standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and handles custom headers while preserving order and duplicates. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective tool fetching.

**Tags:** `http` `proxy` `integration`
