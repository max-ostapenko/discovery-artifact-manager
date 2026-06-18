---
date: 2026-06-18
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible Custom Parameters for BigQuery Connections"
impact: medium
breaking: false
tags: ["BigQuery", "Data Connectivity", "API Update"]
interesting_score: 6
---

# Flexible Custom Parameters for BigQuery Connections

**Date:** 2026-06-18  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary name-value pairs for connector and authentication configurations, allowing for more granular control over external data source settings.

## Details

The update introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps use the new `ConnectorConfigurationParameterValue` type, which supports boolean, double, int32, string, and secret values. Developers can update individual parameters using the `update_mask` in `UpdateConnection`. Notably, the API now supports backtick-escaped parameter IDs (e.g., `configuration.parameters.`parameter id``) for keys that do not fit standard alphanumeric patterns.

**Tags:** `BigQuery` `Data Connectivity` `API Update`
