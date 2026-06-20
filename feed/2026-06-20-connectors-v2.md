---
date: 2026-06-20
api: connectors.v2
service: Application Integration Connectors
title: "Generic HTTP request execution added to Connectors"
impact: high
breaking: false
tags: ["Connectors", "HTTP", "Integration"]
interesting_score: 8
---

# Generic HTTP request execution added to Connectors

**Date:** 2026-06-20  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new `executeHttpRequest` method allows developers to bypass specific connector actions and send raw HTTP requests directly through an established connection.

## Details

The `connectors.v2` API now includes `projects.locations.connections.executeHttpRequest`. This method supports standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, etc.) and accepts a `rawBody` as bytes, enabling support for REST/JSON, GraphQL, XML, and SOAP. It also introduces `ExecuteHttpRequestRequest` and `ExecuteHttpRequestResponse` schemas for handling headers and status codes. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective tool fetching.

**Tags:** `Connectors` `HTTP` `Integration`
