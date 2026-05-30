---
date: 2026-05-30
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameter maps for Connector Configurations"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Flexible parameter maps for Connector Configurations

**Date:** 2026-05-30  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both general connector settings and authentication, allowing for more granular and connector-specific configurations.

## Details

New `parameters` fields have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These fields are maps that accept a new `ConnectorConfigurationParameterValue` type, which functions as a union for `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (secrets are restricted to authentication blocks). Developers can now update specific parameters individually via `ConnectionService.UpdateConnection` by targeting the parameter ID in the `update_mask`, including support for backtick-escaping IDs with special characters.

**Tags:** `bigquery` `connectors` `configuration`
