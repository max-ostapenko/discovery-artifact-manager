---
date: 2026-06-21
api: connectors.v2
service: Application Integration Connectors
title: "Connectors v2 adds raw HTTP execution support"
impact: medium
breaking: false
tags: ["integration", "http", "proxy"]
interesting_score: 8
---

# Connectors v2 adds raw HTTP execution support

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows sending arbitrary HTTP requests through existing connections, supporting any payload format from GraphQL to SOAP.

## Details

Developers can now use the `projects.locations.connections.executeHttpRequest` method to send raw byte payloads (`rawBody`) with custom headers and standard HTTP methods (GET, POST, PUT, etc.). This effectively turns a Connector into a generic proxy for its target system, bypassing the need for specific schema modeling for every endpoint. Additionally, the `tools.list` method now supports a `toolNames` query parameter, allowing for selective fetching of tool definitions rather than retrieving the entire list.

**Tags:** `integration` `http` `proxy`
