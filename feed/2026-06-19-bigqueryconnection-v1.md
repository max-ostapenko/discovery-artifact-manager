---
date: 2026-06-19
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "authentication"]
interesting_score: 6
---

# Flexible parameters for Connector Configurations

**Date:** 2026-06-19  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both general connector configuration and authentication, enabling vendor-specific settings.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` object, which supports multiple data types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter being restricted to authentication blocks). Developers can target specific parameters during updates using the `update_mask` in `ConnectionService.UpdateConnection`, with support for backtick-escaping parameter IDs that contain special characters.

**Tags:** `bigquery` `connectors` `authentication`
