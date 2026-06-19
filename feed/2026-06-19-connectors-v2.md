---
date: 2026-06-19
api: connectors.v2
service: Application Integration Connectors
title: "Connectors v2 adds raw HTTP request execution"
impact: medium
breaking: false
tags: ["integration", "http-client", "api-design"]
interesting_score: 7
---

# Connectors v2 adds raw HTTP request execution

**Date:** 2026-06-19  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows developers to send arbitrary HTTP requests through existing connections, acting as a powerful escape hatch for unsupported API actions.

## Details

The addition of `projects.locations.connections.executeHttpRequest` enables sending raw byte payloads to support REST, GraphQL, XML, SOAP, and Multipart formats. The method supports standard HTTP verbs (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) and handles custom headers while preserving order and duplicates. Additionally, the `tools.list` method now includes a `toolNames` query parameter, allowing for selective fetching of specific tools rather than retrieving the entire list.

**Tags:** `integration` `http-client` `api-design`
