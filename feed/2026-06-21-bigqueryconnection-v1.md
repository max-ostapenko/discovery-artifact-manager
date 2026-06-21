---
date: 2026-06-21
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible Custom Parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Configuration"]
interesting_score: 6
---

# Flexible Custom Parameters for Connector Configurations

**Date:** 2026-06-21  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection now supports arbitrary name-value pairs for both general connector settings and authentication, allowing for more extensible configuration.

## Details

The API introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize the new `ConnectorConfigurationParameterValue` schema, which supports typed values including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue`. This change allows developers to pass connector-specific settings that aren't part of the standard schema. Updates to these parameters via `UpdateConnection` require a specific `update_mask` syntax, and parameter IDs containing special characters must be escaped with backticks.

**Tags:** `BigQuery` `Connectors` `Configuration`
