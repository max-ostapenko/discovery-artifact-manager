---
date: 2026-06-16
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Custom parameters added to Connector Configurations"
impact: medium
breaking: false
tags: ["bigquery", "external-data", "configuration"]
interesting_score: 6
---

# Custom parameters added to Connector Configurations

**Date:** 2026-06-16  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both connector configurations and authentication, allowing for more flexible external data source setups.

## Details

Two new `parameters` fields have been added to `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These fields accept a map of `ConnectorConfigurationParameterValue` objects, which can hold `boolValue`, `doubleValue`, `int32Value`, `stringValue`, or `secretValue` (secrets are restricted to authentication blocks). Developers can target specific parameters during updates using the `update_mask` parameter in `ConnectionService.UpdateConnection`, including support for backtick-escaped parameter IDs for keys containing special characters.

**Tags:** `bigquery` `external-data` `configuration`
