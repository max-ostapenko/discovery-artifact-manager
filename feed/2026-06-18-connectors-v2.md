---
date: 2026-06-18
api: connectors.v2
service: Application Integration Connectors
title: "New generic HTTP execution method for Connectors"
impact: medium
breaking: false
tags: ["integration", "connectors", "http", "rest"]
interesting_score: 8
---

# New generic HTTP execution method for Connectors

**Date:** 2026-06-18  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

Connectors v2 now supports a generic `executeHttpRequest` method, providing an 'escape hatch' to send raw HTTP requests through established connections.

## Details

The new `executeHttpRequest` method on the `connections` resource allows developers to bypass specific connector actions and send raw payloads (REST, GraphQL, XML, SOAP, or Multipart) directly. It accepts a `rawBody` as bytes, a list of `headers`, and a fully resolved `url`. On the response side, it returns the raw `body`, `statusCode`, and `headers`. Additionally, the `tools.list` method now includes a `toolNames` query parameter for selective tool fetching.

**Tags:** `integration` `connectors` `http` `rest`
