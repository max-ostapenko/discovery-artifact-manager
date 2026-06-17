---
date: 2026-06-17
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "Connectors"]
interesting_score: 6
---

# Flexible parameters for Connector Configurations

**Date:** 2026-06-17  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for both general connector configuration and authentication, enabling non-standardized settings.

## Details

The update introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize the new `ConnectorConfigurationParameterValue` schema, which supports boolean, double, int32, string, and secret values. Developers can now pass connector-specific settings that aren't part of the standard schema. Notably, `secretValue` is restricted to authentication parameters. The API also adds support for granular updates via `update_mask` (e.g., `configuration.parameters.parameter_id`) and specifies backtick escaping for parameter IDs with special characters.

**Tags:** `BigQuery` `Data Integration` `Connectors`
