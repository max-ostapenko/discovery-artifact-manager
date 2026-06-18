---
date: 2026-06-18
api: connectors.v2
service: App Integration Connectors
title: "Generic HTTP execution arrives in Connectors v2"
impact: high
breaking: false
tags: ["integrations", "http", "api-design"]
interesting_score: 8
---

# Generic HTTP execution arrives in Connectors v2

**Date:** 2026-06-18  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to bypass specific connector actions and send arbitrary HTTP requests through established connections.

## Details

The Connectors API has introduced a powerful escape hatch: `executeHttpRequest`. This method allows you to send raw payloads (REST, GraphQL, XML, SOAP, or Multipart) directly to a connection's target. The request schema (`ExecuteHttpRequestRequest`) supports standard HTTP methods, custom headers, and a `rawBody` byte field. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective tool fetching, improving performance when dealing with large toolsets.

**Tags:** `integrations` `http` `api-design`
