---
date: 2026-06-17
api: connectors.v2
service: Integration Connectors
title: "Raw HTTP escape hatch added to Connectors"
impact: high
breaking: false
tags: ["integration", "rest", "graphql", "connectivity"]
interesting_score: 8
---

# Raw HTTP escape hatch added to Connectors

**Date:** 2026-06-17  
**API:** `connectors.v2`  
**Impact:** High  

## Summary

A new executeHttpRequest method allows developers to bypass structured connector actions and send raw HTTP requests directly through an established connection.

## Details

The addition of `projects.locations.connections.executeHttpRequest` provides a generic interface for interacting with backends. It supports standard verbs (GET, POST, PUT, PATCH, DELETE, etc.) and accepts a `rawBody` as bytes, enabling support for any payload format including GraphQL, SOAP, and XML. The request and response schemas include full header support and status code reporting. Additionally, the tools `list` method now includes a `toolNames` query parameter for selective tool fetching.

**Tags:** `integration` `rest` `graphql` `connectivity`
