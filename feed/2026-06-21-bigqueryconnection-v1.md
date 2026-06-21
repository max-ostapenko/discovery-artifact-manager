---
date: 2026-06-21
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Custom parameters for BigQuery Connections"
impact: medium
breaking: false
tags: ["BigQuery", "Data Connectors", "API Update"]
interesting_score: 6
---

# Custom parameters for BigQuery Connections

**Date:** 2026-06-21  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for connector and authentication configurations, enabling more flexible data source setups.

## Details

New `parameters` maps have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps allow developers to pass connector-specific settings that aren't part of the standard schema using the new `ConnectorConfigurationParameterValue` type, which supports strings, booleans, integers, doubles, and secrets. When updating these via `UpdateConnection`, developers should use the `update_mask` with the specific parameter ID, ensuring IDs with special characters are escaped with backticks.

**Tags:** `BigQuery` `Data Connectors` `API Update`
