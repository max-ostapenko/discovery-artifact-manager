---
date: 2026-05-29
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Custom parameters for BigQuery Connectors"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Custom parameters for BigQuery Connectors

**Date:** 2026-05-29  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for connector configurations and authentication, allowing for more flexible, source-specific settings.

## Details

New `parameters` maps have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps use the new `ConnectorConfigurationParameterValue` schema, which supports boolean, double, int32, string, and secret values. This allows developers to pass non-standardized configuration options directly to connectors. Notably, the API supports granular updates to these parameters via `update_mask`, including a syntax for escaping parameter IDs that contain special characters or spaces using backticks (e.g., `configuration.parameters.`parameter id``).

**Tags:** `bigquery` `connectors` `configuration`
