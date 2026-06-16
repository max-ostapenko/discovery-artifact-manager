---
date: 2026-06-16
api: connectors.v2
service: Application Integration Connectors
title: "New generic HTTP escape hatch for Connectors"
impact: high
breaking: false
tags: ["integration", "http", "api-design"]
interesting_score: 8
---

# New generic HTTP escape hatch for Connectors

**Date:** 2026-06-16  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

Connectors v2 now supports a generic executeHttpRequest method, allowing developers to send raw HTTP requests directly through established connections.

## Details

The new `executeHttpRequest` method on the `connections` resource provides a powerful escape hatch for scenarios where a specific connector action isn't available. It supports REST, GraphQL, XML, and SOAP by accepting a `rawBody` as bytes, along with a full suite of HTTP methods (GET, POST, PUT, PATCH, DELETE, etc.). Developers must provide a fully resolved URL and can pass custom headers. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective fetching of tool definitions.

**Tags:** `integration` `http` `api-design`
