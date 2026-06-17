---
date: 2026-06-17
api: connectors.v2
service: Application Integration Connectors
title: "New raw HTTP execution escape hatch for Connectors"
impact: medium
breaking: false
tags: ["integrations", "http", "api-design"]
interesting_score: 8
---

# New raw HTTP execution escape hatch for Connectors

**Date:** 2026-06-17  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method, allowing developers to send raw HTTP payloads directly through established connections.

## Details

The new `executeHttpRequest` method on the `connections` resource provides a powerful 'escape hatch' for scenarios where a specific connector action doesn't exist. It supports GET, POST, PUT, PATCH, DELETE, HEAD, and OPTIONS. Developers can pass a `rawBody` as bytes, enabling support for REST/JSON, GraphQL, XML, SOAP, and Multipart formats. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective tool fetching, improving performance when only specific metadata is needed.

**Tags:** `integrations` `http` `api-design`
