---
date: 2026-06-14
api: connectors.v2
service: Application Integration Connectors
title: "New executeHttpRequest method for raw HTTP calls"
impact: medium
breaking: false
tags: ["Integration", "Connectors", "HTTP"]
interesting_score: 7
---

# New executeHttpRequest method for raw HTTP calls

**Date:** 2026-06-14  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

Developers can now execute generic HTTP requests directly through existing connections, bypassing specific connector schemas for REST, GraphQL, SOAP, and more.

## Details

The new `executeHttpRequest` method on the `connections` resource allows for raw byte-level interaction with backends. It supports standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, etc.) and handles custom headers and raw payloads. This is particularly useful for interacting with endpoints not fully modeled by a specific connector. Additionally, the `tools.list` method now includes a `toolNames` parameter to allow for selective fetching of tool definitions.

**Tags:** `Integration` `Connectors` `HTTP`
