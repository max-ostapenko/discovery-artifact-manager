---
date: 2026-06-17
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible, typed parameters for BigQuery Connections"
impact: medium
breaking: false
tags: ["BigQuery", "External Data", "Configuration"]
interesting_score: 6
---

# Flexible, typed parameters for BigQuery Connections

**Date:** 2026-06-17  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary, typed configuration and authentication parameters via a new parameters map, enabling connector-specific settings.

## Details

New `parameters` fields have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize the new `ConnectorConfigurationParameterValue` schema, which supports `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter being restricted to authentication). This allows developers to pass non-standardized configuration options to external data sources. The API also supports updating individual parameters via `UpdateConnection` using an `update_mask` with backtick-escaped IDs for complex parameter names.

**Tags:** `BigQuery` `External Data` `Configuration`
