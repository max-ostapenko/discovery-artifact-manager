---
date: 2026-06-02
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible custom parameters for BigQuery Connections"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "Connectors"]
interesting_score: 6
---

# Flexible custom parameters for BigQuery Connections

**Date:** 2026-06-02  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both connector and authentication configurations, enabling more granular control over non-standardized settings.

## Details

This update introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize a new `ConnectorConfigurationParameterValue` schema, which supports typed values including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (secrets are exclusive to authentication). Developers can target specific parameters during updates using the `update_mask` in `ConnectionService.UpdateConnection`, with support for backtick-escaping parameter IDs that contain special characters.

**Tags:** `BigQuery` `Data Integration` `Connectors`
