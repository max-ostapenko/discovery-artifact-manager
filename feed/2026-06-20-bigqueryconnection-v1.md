---
date: 2026-06-20
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameters added to Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Authentication"]
interesting_score: 6
---

# Flexible parameters added to Connector Configurations

**Date:** 2026-06-20  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for connector and authentication configurations, allowing for more granular and non-standard settings.

## Details

The update introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps use the new `ConnectorConfigurationParameterValue` type, which supports boolean, double, int32, string, and secret values. Developers can update individual parameters using a specific `update_mask` format in `UpdateConnection` (e.g., `configuration.parameters.parameter_id`), including support for backtick-escaped parameter IDs if they contain special characters.

**Tags:** `BigQuery` `Connectors` `Authentication`
