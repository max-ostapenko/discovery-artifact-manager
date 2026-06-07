---
date: 2026-06-07
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Custom parameters added to Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Data Integration"]
interesting_score: 6
---

# Custom parameters added to Connector Configurations

**Date:** 2026-06-07  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for connector and authentication configurations, enabling more flexible integration with external data sources.

## Details

The update introduces a 'parameters' map to both 'ConnectorConfiguration' and 'ConnectorConfigurationAuthentication' schemas. These maps use the new 'ConnectorConfigurationParameterValue' type, which supports boolean, double, int32, string, and secret values. Developers can update individual parameters using the 'update_mask' in 'ConnectionService.UpdateConnection', with support for backtick-escaped parameter IDs for keys that do not fit standard naming patterns.

**Tags:** `BigQuery` `Connectors` `Data Integration`
