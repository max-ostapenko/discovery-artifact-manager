---
date: 2026-06-02
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible typed parameters for connector configurations"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Flexible typed parameters for connector configurations

**Date:** 2026-06-02  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connections now support arbitrary key-value parameters for both general connector configuration and authentication, allowing for more extensible connector setups.

## Details

The API has introduced a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps use the new `ConnectorConfigurationParameterValue` type, which supports a variety of scalars including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and a `secretValue` (reserved for authentication). This change allows developers to pass non-standardized configuration settings to connectors without waiting for schema updates. Notably, the API now supports granular updates to these parameters via `update_mask` and requires backtick escaping for parameter IDs containing special characters.

**Tags:** `bigquery` `connectors` `configuration`
