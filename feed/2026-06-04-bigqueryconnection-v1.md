---
date: 2026-06-04
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Custom parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Authentication"]
interesting_score: 6
---

# Custom parameters for Connector Configurations

**Date:** 2026-06-04  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for connector configurations and authentication, enabling more flexible, connector-specific settings.

## Details

New `parameters` fields have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These fields are maps of name-value pairs using the new `ConnectorConfigurationParameterValue` schema, which supports a variety of types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue`. Developers can target specific parameters during updates by using the `update_mask` in `ConnectionService.UpdateConnection`, with support for backtick-escaping parameter IDs that contain special characters.

**Tags:** `BigQuery` `Connectors` `Authentication`
