---
date: 2026-06-19
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible connector-specific parameters added"
impact: medium
breaking: false
tags: ["BigQuery", "Data Connectivity", "Configuration"]
interesting_score: 6
---

# Flexible connector-specific parameters added

**Date:** 2026-06-19  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for both general connector configuration and authentication, enabling support for non-standard connector settings.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type, which supports a variety of data types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and a specialized `secretValue` for authentication. Developers can target specific parameters during updates using the `update_mask` in `ConnectionService.UpdateConnection`, including support for backtick-escaped parameter IDs.

**Tags:** `BigQuery` `Data Connectivity` `Configuration`
