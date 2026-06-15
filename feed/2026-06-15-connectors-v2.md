---
date: 2026-06-15
api: connectors.v2
service: Application Integration Connectors
title: "Connectors v2 adds generic HTTP request execution"
impact: high
breaking: false
tags: ["integration", "http", "api-design"]
interesting_score: 8
---

# Connectors v2 adds generic HTTP request execution

**Date:** 2026-06-15  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to send arbitrary HTTP requests through a connection, supporting any payload format via raw bytes.

## Details

The API now includes a powerful 'escape hatch' via the `executeHttpRequest` method on connection resources. This method supports standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, etc.) and accepts a `rawBody` byte field, enabling developers to interact with endpoints using GraphQL, XML, SOAP, or custom JSON structures that aren't explicitly modeled in the connector's schema. Additionally, the `tools.list` method gained a `toolNames` query parameter for selective fetching of tool definitions.

**Tags:** `integration` `http` `api-design`
