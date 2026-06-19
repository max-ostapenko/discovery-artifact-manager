---
date: 2026-06-19
api: connectors.v2
service: Application Integration Connectors
title: "Connectors v2 adds raw HTTP request 'escape hatch'"
impact: high
breaking: false
tags: ["Integration", "Connectors", "HTTP"]
interesting_score: 8
---

# Connectors v2 adds raw HTTP request 'escape hatch'

**Date:** 2026-06-19  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to bypass predefined connector actions and send arbitrary HTTP requests through existing connections.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a generic interface for REST, GraphQL, XML, SOAP, and Multipart payloads. It accepts a `rawBody` (bytes), `httpMethod`, and a list of `headers`, returning the full response including status codes and reason phrases. Additionally, the `tools.list` method now supports a `toolNames` repeated query parameter for selective tool fetching.

**Tags:** `Integration` `Connectors` `HTTP`
