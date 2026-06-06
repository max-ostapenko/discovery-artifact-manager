---
date: 2026-06-06
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible connector and auth parameters added"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Authentication"]
interesting_score: 6
---

# Flexible connector and auth parameters added

**Date:** 2026-06-06  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both general connector configuration and authentication, allowing for non-standardized settings.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type which supports a variety of scalar types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter being restricted to authentication blocks). Developers can update individual parameters using specific update masks, such as `configuration.parameters.parameter_id`, and the API now explicitly supports backtick escaping for parameter IDs that contain special characters.

**Tags:** `BigQuery` `Connectors` `Authentication`
