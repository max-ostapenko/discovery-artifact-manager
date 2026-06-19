---
date: 2026-06-19
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Custom parameters added to Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Data Connectors", "Configuration"]
interesting_score: 6
---

# Custom parameters added to Connector Configurations

**Date:** 2026-06-19  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary name-value pairs for both general connector configuration and authentication, enabling more flexible, connector-specific settings.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type, which supports typed values including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter is reserved for authentication). Developers can update individual parameters using the `update_mask` in `ConnectionService.UpdateConnection`, with support for backtick-escaped parameter IDs if they contain special characters.

**Tags:** `BigQuery` `Data Connectors` `Configuration`
