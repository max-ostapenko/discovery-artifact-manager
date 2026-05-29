---
date: 2026-05-29
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible custom parameters for BigQuery Connectors"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Flexible custom parameters for BigQuery Connectors

**Date:** 2026-05-29  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for connector and authentication configurations, including typed values and secrets.

## Details

The update introduces a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps use the new `ConnectorConfigurationParameterValue` type, which supports boolean, double, int32, string, and secret values. Developers can update individual parameters using the `update_mask` in `ConnectionService.UpdateConnection`. Notably, if a parameter ID contains special characters, it must be escaped with backticks (e.g., `configuration.parameters.`parameter id``).

**Tags:** `bigquery` `connectors` `configuration`
