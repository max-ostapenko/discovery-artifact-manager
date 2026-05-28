---
date: 2026-05-28
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible connector-specific parameters added"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Flexible connector-specific parameters added

**Date:** 2026-05-28  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection now supports arbitrary key-value parameters for both general connector configuration and authentication, allowing for more granular, connector-specific settings.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` object which supports multiple data types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter is restricted to authentication parameters). Developers can update individual parameters using an `update_mask` in `UpdateConnection` calls, and the API now explicitly supports backtick escaping for parameter IDs that contain special characters.

**Tags:** `bigquery` `connectors` `configuration`
