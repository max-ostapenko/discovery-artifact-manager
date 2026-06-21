---
date: 2026-06-21
api: connectors.v2
service: App Integration Connectors
title: "Raw HTTP execution support added to Connectors"
impact: medium
breaking: false
tags: ["integration", "http", "api-design"]
interesting_score: 8
---

# Raw HTTP execution support added to Connectors

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new `executeHttpRequest` method allows developers to bypass structured connector schemas and send raw HTTP requests through existing connections.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a powerful 'escape hatch' for integration developers. It supports standard HTTP methods (GET, POST, PUT, PATCH, DELETE, etc.) and accepts a `rawBody` as bytes, enabling support for GraphQL, SOAP, XML, and Multipart payloads that might not be natively modeled in a specific connector. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective fetching of tool definitions.

**Tags:** `integration` `http` `api-design`
