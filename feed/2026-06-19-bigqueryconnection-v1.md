---
date: 2026-06-19
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible key-value parameters for BigQuery Connectors"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "Connectors"]
interesting_score: 6
---

# Flexible key-value parameters for BigQuery Connectors

**Date:** 2026-06-19  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary, typed parameters for connector and authentication configurations, enabling more extensible external data source setups.

## Details

New `parameters` maps have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize a new `ConnectorConfigurationParameterValue` schema, which acts as a container for various types including `stringValue`, `boolValue`, `int32Value`, `doubleValue`, and `secretValue` (the latter being exclusive to authentication). This change allows developers to pass connector-specific settings that aren't part of the standard schema. Updates are also more granular; you can now target specific parameters in an `UpdateConnection` call using an `update_mask` like `configuration.parameters.my_param_id`.

**Tags:** `BigQuery` `Data Integration` `Connectors`
