---
date: 2026-06-21
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["bigquery", "connections", "connectors"]
interesting_score: 6
---

# Flexible parameters for Connector Configurations

**Date:** 2026-06-21  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection now supports arbitrary key-value parameters for both general connector configuration and authentication, allowing for non-standard connector settings.

## Details

The API introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize the new `ConnectorConfigurationParameterValue` schema, which supports strongly-typed values including booleans, doubles, integers, strings, and secrets (restricted to authentication). Developers can update individual parameters using granular `update_mask` paths like `configuration.parameters.parameter_id`. Notably, the API now supports backtick escaping for parameter IDs that contain spaces or special characters.

**Tags:** `bigquery` `connections` `connectors`
