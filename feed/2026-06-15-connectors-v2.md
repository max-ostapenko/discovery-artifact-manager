---
date: 2026-06-15
api: connectors.v2
service: Application Integration Connectors
title: "Connectors v2 adds generic HTTP request execution"
impact: medium
breaking: false
tags: ["Connectors", "HTTP", "Integration"]
interesting_score: 7
---

# Connectors v2 adds generic HTTP request execution

**Date:** 2026-06-15  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows developers to send raw HTTP requests through existing connections, supporting any payload format from REST to SOAP.

## Details

The API now includes `projects.locations.connections.executeHttpRequest`, a flexible method for bypass scenarios where standard connector schemas are insufficient. It accepts an `ExecuteHttpRequestRequest` object containing a target URL, HTTP method (GET, POST, PUT, etc.), custom headers, and a `rawBody` as bytes. This enables support for GraphQL, XML, SOAP, and Multipart payloads directly through the connector infrastructure. Additionally, the `tools.list` method now supports a `toolNames` repeated query parameter for selective tool fetching.

**Tags:** `Connectors` `HTTP` `Integration`
