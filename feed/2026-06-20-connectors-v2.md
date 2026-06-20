---
date: 2026-06-20
api: connectors.v2
service: Connectors
title: "Generic HTTP Request Execution for Connectors"
impact: medium
breaking: false
tags: ["Application Integration", "Connectors", "HTTP", "REST"]
interesting_score: 8
---

# Generic HTTP Request Execution for Connectors

**Date:** 2026-06-20  
**API:** `connectors.v2`  
**Impact:** Medium  

## Summary

A new executeHttpRequest method allows developers to send raw HTTP requests through existing connections, supporting any payload format from REST to SOAP.

## Details

The executeHttpRequest method has been added to the connections resource, enabling raw HTTP interactions (GET, POST, PUT, PATCH, DELETE, etc.) using the connection's underlying authentication. It accepts a rawBody byte payload, allowing for REST/JSON, GraphQL, XML, and SOAP requests. Additionally, the tools.list method now includes a toolNames parameter for selective tool fetching, improving efficiency when working with large toolsets.

**Tags:** `Application Integration` `Connectors` `HTTP` `REST`
