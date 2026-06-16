---
date: 2026-06-16
api: connectors.v2
service: Application Integration Connectors
title: "New raw HTTP escape hatch for Connectors"
impact: medium
breaking: false
tags: ["integration", "http", "api-design"]
interesting_score: 8
---

# New raw HTTP escape hatch for Connectors

**Date:** 2026-06-16  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method, allowing developers to send raw payloads including GraphQL, SOAP, and XML through existing connections.

## Details

The new `executeHttpRequest` method on the connection resource provides a powerful 'escape hatch' for scenarios where standard connector actions are insufficient. It accepts a `rawBody` (bytes), `httpMethod`, and custom `headers`, returning the full response including status codes and raw bytes. Additionally, the `tools.list` method has been updated with a `toolNames` parameter to allow for selective fetching of specific tools.

**Tags:** `integration` `http` `api-design`
