---
date: 2026-06-12
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Dynamic connector-specific parameters added"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Authentication"]
interesting_score: 6
---

# Dynamic connector-specific parameters added

**Date:** 2026-06-12  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection now supports arbitrary, typed parameters for connector and authentication configurations, allowing for more flexible integration with external data sources.

## Details

The API introduces a flexible 'parameters' map to both ConnectorConfiguration and ConnectorConfigurationAuthentication schemas. These maps utilize the new ConnectorConfigurationParameterValue object, which supports boolean, double, int32, string, and secret values. This change allows developers to pass non-standardized configuration settings to connectors. Notably, the API now supports granular updates via update_mask (e.g., configuration.parameters.parameter_id) and requires backtick escaping for parameter IDs containing special characters.

**Tags:** `BigQuery` `Connectors` `Authentication`
