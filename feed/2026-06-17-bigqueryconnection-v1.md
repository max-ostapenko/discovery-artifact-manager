---
date: 2026-06-17
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible Custom Parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "Connectors"]
interesting_score: 6
---

# Flexible Custom Parameters for Connector Configurations

**Date:** 2026-06-17  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connections now support arbitrary, typed parameters for both general connector and authentication configurations.

## Details

The API has introduced a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps allow developers to pass custom name-value pairs using the new `ConnectorConfigurationParameterValue` type, which supports boolean, double, int32, string, and secret values. This is particularly useful for passing non-standard configuration settings to external data sources. Developers can update specific parameters using an `update_mask` and should note that `secretValue` is exclusively permitted within authentication parameters.

**Tags:** `BigQuery` `Data Integration` `Connectors`
