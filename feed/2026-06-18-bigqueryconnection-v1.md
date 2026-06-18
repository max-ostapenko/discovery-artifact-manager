---
date: 2026-06-18
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible Custom Parameters for BigQuery Connections"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "API Update"]
interesting_score: 6
---

# Flexible Custom Parameters for BigQuery Connections

**Date:** 2026-06-18  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for connector and authentication configurations, enabling more granular control over non-standardized settings.

## Details

Both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` have gained a `parameters` field, which is a map of name-value pairs. These values are defined by the new `ConnectorConfigurationParameterValue` schema, supporting `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (for auth). Developers can update specific parameters individually using the `update_mask` in `ConnectionService.UpdateConnection`, with support for backtick-escaping parameter IDs that contain special characters.

**Tags:** `BigQuery` `Data Integration` `API Update`
