---
date: 2026-06-21
api: connectors.v2
service: App Integration Connectors
title: "Connectors v2 adds generic HTTP execution escape hatch"
impact: high
breaking: false
tags: ["Integration", "HTTP", "GraphQL", "SOAP"]
interesting_score: 8
---

# Connectors v2 adds generic HTTP execution escape hatch

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows for raw HTTP calls through connections, supporting any payload format including GraphQL and SOAP.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a flexible way to interact with backends that may not have specific actions defined. It accepts an `ExecuteHttpRequestRequest` containing a `rawBody` (bytes), custom `headers`, and a target `url`. The response includes the raw `body`, `statusCode`, and `headers`. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective tool fetching, improving performance when you only need specific metadata.

**Tags:** `Integration` `HTTP` `GraphQL` `SOAP`
