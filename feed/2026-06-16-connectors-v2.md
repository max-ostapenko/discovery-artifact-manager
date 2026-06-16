---
date: 2026-06-16
api: connectors.v2
service: App Integration Connectors
title: "Connectors v2 adds raw HTTP execution capability"
impact: medium
breaking: false
tags: ["integration", "http", "connectors"]
interesting_score: 8
---

# Connectors v2 adds raw HTTP execution capability

**Date:** 2026-06-16  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows developers to send arbitrary HTTP payloads through existing connections, bypassing specific connector schemas.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a generic escape hatch for interacting with backends. It supports all standard HTTP methods (GET, POST, PUT, etc.) and handles raw byte payloads, making it compatible with REST, GraphQL, XML, and SOAP. The request schema `ExecuteHttpRequestRequest` requires a fully resolved URL and allows custom headers. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective metadata fetching.

**Tags:** `integration` `http` `connectors`
