---
date: 2026-06-18
api: connectors.v2
service: Application Integration Connectors
title: "Generic HTTP execution added to Connectors v2"
impact: high
breaking: false
tags: ["integration", "http", "api-design"]
interesting_score: 8
---

# Generic HTTP execution added to Connectors v2

**Date:** 2026-06-18  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to send raw HTTP requests through a connection, supporting any payload format and standard HTTP methods.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a powerful 'escape hatch' for developers. It supports standard verbs (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and accepts a `rawBody` as bytes, enabling support for REST, GraphQL, XML, SOAP, and Multipart payloads through the connector's existing authentication context. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective tool fetching.

**Tags:** `integration` `http` `api-design`
