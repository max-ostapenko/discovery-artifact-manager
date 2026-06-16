---
date: 2026-06-16
api: connectors.v2
service: Application Integration Connectors
title: "Generic HTTP execution added to Connectors v2"
impact: high
breaking: false
tags: ["Integration", "HTTP", "Connectors"]
interesting_score: 8
---

# Generic HTTP execution added to Connectors v2

**Date:** 2026-06-16  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

New `executeHttpRequest` method enables arbitrary HTTP calls through connections, supporting REST, GraphQL, and SOAP via raw byte payloads.

## Details

The `executeHttpRequest` method on the connection resource provides a flexible way to interact with backends that don't have specific actions defined. It supports standard HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and handles raw byte payloads for `rawBody`, making it compatible with XML, SOAP, and Multipart formats. Additionally, the `tools.list` method now supports a `toolNames` query parameter for selective tool fetching, allowing developers to optimize tool discovery.

**Tags:** `Integration` `HTTP` `Connectors`
