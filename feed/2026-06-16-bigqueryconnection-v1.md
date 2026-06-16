---
date: 2026-06-16
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Dynamic parameters added to Connector Configurations"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Dynamic parameters added to Connector Configurations

**Date:** 2026-06-16  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both general connector configuration and authentication, enabling more flexible external data source setups.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` object that supports multiple data types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter specifically for authentication). Developers can target specific parameters during updates by using the `update_mask` in `ConnectionService.UpdateConnection`, and the API now explicitly supports backtick escaping for parameter IDs that contain non-standard characters.

**Tags:** `bigquery` `connectors` `configuration`
