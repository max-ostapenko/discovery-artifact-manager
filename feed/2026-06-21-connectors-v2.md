---
date: 2026-06-21
api: connectors.v2
service: Application Connectors
title: "Raw HTTP execution support for Connections"
impact: medium
breaking: false
tags: ["integration", "http", "api-design"]
interesting_score: 7
---

# Raw HTTP execution support for Connections

**Date:** 2026-06-21  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows developers to bypass specific connector schemas and perform generic HTTP calls through existing connections.

## Details

The addition of projects.locations.connections.executeHttpRequest enables raw byte-level interaction with backends, supporting REST, GraphQL, XML, SOAP, and Multipart payloads. The method accepts a fully resolved URL, standard HTTP methods (GET, POST, etc.), and custom headers via the ExecuteHttpRequestRequest schema. Additionally, the tools.list method now includes a toolNames query parameter, allowing for selective fetching of specific tools rather than retrieving the entire list.

**Tags:** `integration` `http` `api-design`
