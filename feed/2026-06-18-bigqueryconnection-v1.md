---
date: 2026-06-18
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Custom parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Data Connectors", "Authentication"]
interesting_score: 6
---

# Custom parameters for Connector Configurations

**Date:** 2026-06-18  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary name-value pairs for connector and authentication configurations, allowing for more flexible, connector-specific settings.

## Details

The `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas now include a `parameters` map. These maps utilize the new `ConnectorConfigurationParameterValue` type, which supports boolean, double, int32, string, and secret values. This addition allows developers to pass non-standardized configuration data to connectors. Notably, `secretValue` is restricted to authentication parameters. Updates to these parameters can be targeted specifically using an `update_mask` in `ConnectionService.UpdateConnection`, with a new syntax for escaping parameter IDs that contain special characters using backticks.

**Tags:** `BigQuery` `Data Connectors` `Authentication`
