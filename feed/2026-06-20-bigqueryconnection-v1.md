---
date: 2026-06-20
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Dynamic parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Authentication", "Configuration"]
interesting_score: 6
---

# Dynamic parameters for Connector Configurations

**Date:** 2026-06-20  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both connector and authentication configurations, enabling more flexible, connector-specific settings.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` object which supports a variety of types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter specifically for authentication). Developers can now update specific parameters via `ConnectionService.UpdateConnection` by using the `update_mask` and escaping non-standard parameter IDs with backticks.

**Tags:** `BigQuery` `Connectors` `Authentication` `Configuration`
