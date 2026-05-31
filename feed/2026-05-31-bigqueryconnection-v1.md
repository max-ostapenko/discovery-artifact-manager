---
date: 2026-05-31
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Data Integration"]
interesting_score: 6
---

# Flexible parameters for Connector Configurations

**Date:** 2026-05-31  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery connections now support arbitrary, connector-specific parameters for both general configuration and authentication blocks.

## Details

The API introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps allow developers to pass non-standardized configuration values using the new `ConnectorConfigurationParameterValue` schema, which supports `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and a `secretValue` (reserved for authentication). Individual parameters can be targeted for updates using an `update_mask` like `configuration.parameters.parameter_id`.

**Tags:** `BigQuery` `Connectors` `Data Integration`
