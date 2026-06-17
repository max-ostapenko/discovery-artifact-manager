---
date: 2026-06-17
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "API Extensibility"]
interesting_score: 6
---

# Flexible parameters for Connector Configurations

**Date:** 2026-06-17  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for connector and authentication configurations, allowing for more granular and custom connector setups.

## Details

The update introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps use the new `ConnectorConfigurationParameterValue` schema, which supports multiple types including boolean, double, int32, string, and secrets (auth-only). Developers can update individual parameters using specific `update_mask` paths like `configuration.parameters.parameter_id`, with support for backtick escaping for non-standard IDs. This effectively allows the API to support connector-specific settings that aren't part of the standardized schema.

**Tags:** `BigQuery` `Connectors` `API Extensibility`
