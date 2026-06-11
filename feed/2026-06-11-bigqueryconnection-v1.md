---
date: 2026-06-11
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Dynamic Parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "Connectors"]
interesting_score: 6
---

# Dynamic Parameters for Connector Configurations

**Date:** 2026-06-11  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for both connector and authentication configurations, enabling support for non-standardized connector settings.

## Details

New `parameters` maps have been added to `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize the newly introduced `ConnectorConfigurationParameterValue` schema, which provides typed support for `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue`. Notably, `secretValue` is restricted to authentication parameters. Developers can update individual parameters via `ConnectionService.UpdateConnection` by specifying an `update_mask` such as `configuration.parameters.parameter_id`, including support for backtick-escaped IDs.

**Tags:** `BigQuery` `Data Integration` `Connectors`
