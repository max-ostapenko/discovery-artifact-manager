---
date: 2026-06-17
api: connectors.v2
service: App Integration Connectors
title: "Connectors v2 adds universal HTTP request execution"
impact: high
breaking: false
tags: ["Connectors", "Integration", "HTTP", "REST"]
interesting_score: 8
---

# Connectors v2 adds universal HTTP request execution

**Date:** 2026-06-17  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new `executeHttpRequest` method allows developers to bypass specific connector schemas and send raw HTTP requests directly through an established connection.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a 'break-glass' capability for interacting with backend systems. It supports standard HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and accepts a `rawBody` byte payload, enabling support for REST, GraphQL, XML, SOAP, and Multipart formats. The API handles headers via the new `HttpHeader` schema, preserving order and allowing duplicate keys. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective tool fetching.

**Tags:** `Connectors` `Integration` `HTTP` `REST`
