---
date: 2026-06-18
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Custom key-value parameters for BigQuery Connectors"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "Connectors"]
interesting_score: 6
---

# Custom key-value parameters for BigQuery Connectors

**Date:** 2026-06-18  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary, typed parameters for connector and authentication configurations, enabling more flexible integration with external data sources.

## Details

Developers can now use the `parameters` map within `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` to pass non-standard configuration values. These values are encapsulated in the new `ConnectorConfigurationParameterValue` schema, which supports `stringValue`, `int32Value`, `doubleValue`, `boolValue`, and `secretValue`. Notably, `UpdateConnection` allows targeting specific parameters in the update mask, such as `configuration.parameters.my_param_id`, with support for backtick escaping for IDs containing special characters.

**Tags:** `BigQuery` `Data Integration` `Connectors`
