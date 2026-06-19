---
date: 2026-06-19
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible Parameters for BigQuery Connections"
impact: medium
breaking: false
tags: ["BigQuery", "Data Connectors", "API Update"]
interesting_score: 6
---

# Flexible Parameters for BigQuery Connections

**Date:** 2026-06-19  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary, typed parameters for connector and authentication configurations, enabling more granular control over non-standard settings.

## Details

The `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas have been updated with a `parameters` map. This map accepts a new `ConnectorConfigurationParameterValue` object, which supports multiple data types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (exclusive to authentication). Developers can update individual parameters using the `update_mask` in `ConnectionService.UpdateConnection`, with support for backtick escaping for parameter IDs that contain special characters.

**Tags:** `BigQuery` `Data Connectors` `API Update`
