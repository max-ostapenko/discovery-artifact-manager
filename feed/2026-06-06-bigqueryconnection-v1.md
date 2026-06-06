---
date: 2026-06-06
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible Key-Value Parameters for Connector Configs"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Configuration"]
interesting_score: 6
---

# Flexible Key-Value Parameters for Connector Configs

**Date:** 2026-06-06  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for connector and authentication configurations, enabling more extensible external data source setups.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` object which supports multiple data types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and a `secretValue` (reserved for authentication). Developers can update individual parameters via `ConnectionService.UpdateConnection` by targeting specific keys in the `update_mask`, with support for backtick escaping for complex parameter IDs.

**Tags:** `BigQuery` `Connectors` `Configuration`
