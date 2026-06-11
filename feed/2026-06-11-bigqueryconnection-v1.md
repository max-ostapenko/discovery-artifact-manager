---
date: 2026-06-11
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameter maps for external connectors"
impact: medium
breaking: false
tags: ["BigQuery", "External Connections", "Configuration"]
interesting_score: 6
---

# Flexible parameter maps for external connectors

**Date:** 2026-06-11  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both connector and authentication configurations.

## Details

New `parameters` fields have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type, which supports a variety of scalar types (string, boolean, int32, double) and a `secretValue` specifically for authentication. This change allows developers to pass custom, connector-specific configuration settings that aren't part of the standardized API schema. Notably, the API now supports granular updates to these parameters via `update_mask`, including a specific syntax for escaping parameter IDs that contain special characters using backticks.

**Tags:** `BigQuery` `External Connections` `Configuration`
