---
date: 2026-06-16
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible connector-specific parameters added"
impact: medium
breaking: false
tags: ["bigquery", "connectivity", "configuration"]
interesting_score: 6
---

# Flexible connector-specific parameters added

**Date:** 2026-06-16  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection now supports arbitrary key-value parameters for both general configuration and authentication, allowing for connector-specific settings not covered by standard schemas.

## Details

The API has introduced `parameters` maps to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize a new `ConnectorConfigurationParameterValue` schema that supports multiple data types: `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter being restricted to authentication blocks). Developers can target specific parameters for updates using the `update_mask` (e.g., `configuration.parameters.parameter_id`) and must use backticks to escape parameter IDs that contain special characters.

**Tags:** `bigquery` `connectivity` `configuration`
