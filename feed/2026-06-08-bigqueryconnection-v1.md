---
date: 2026-06-08
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Authentication"]
interesting_score: 6
---

# Flexible parameters for Connector Configurations

**Date:** 2026-06-08  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection now supports arbitrary key-value parameters for connector and authentication configurations, enabling specialized settings and secret management.

## Details

New `parameters` maps have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize the new `ConnectorConfigurationParameterValue` schema, which supports typed values including boolean, double, int32, string, and a specific `secretValue` for authentication. Developers can update individual parameters via `ConnectionService.UpdateConnection` using an `update_mask`, and the API now supports backtick-escaped parameter IDs for keys with special characters.

**Tags:** `BigQuery` `Connectors` `Authentication`
