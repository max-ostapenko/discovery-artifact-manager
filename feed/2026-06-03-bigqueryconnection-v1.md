---
date: 2026-06-03
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Configuration"]
interesting_score: 6
---

# Flexible parameters for Connector Configurations

**Date:** 2026-06-03  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for connector and authentication configurations, enabling more granular control over external data source settings.

## Details

New `parameters` maps have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type, which supports a variety of scalar types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and a `secretValue` (exclusive to authentication). Developers can target specific parameters during updates using the `update_mask` in `ConnectionService.UpdateConnection`, and the API now supports backtick-escaping for parameter IDs that contain special characters.

**Tags:** `BigQuery` `Connectors` `Configuration`
