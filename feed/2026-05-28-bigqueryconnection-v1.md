---
date: 2026-05-28
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible Connector Parameters and Authentication"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Flexible Connector Parameters and Authentication

**Date:** 2026-05-28  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery connections now support arbitrary, connector-specific configuration and authentication parameters via a new map-based schema.

## Details

The API has added a `parameters` field to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. This field allows for a map of name-value pairs using the new `ConnectorConfigurationParameterValue` schema, which supports multiple data types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue`. This change enables developers to pass non-standardized configuration options to connectors and perform granular updates using an `update_mask` (e.g., `configuration.parameters.parameter_id`).

**Tags:** `bigquery` `connectors` `configuration`
