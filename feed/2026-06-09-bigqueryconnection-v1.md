---
date: 2026-06-09
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible connector and auth parameters added"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "Authentication", "Secrets"]
interesting_score: 6
---

# Flexible connector and auth parameters added

**Date:** 2026-06-09  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for connector configurations and authentication, allowing for non-standardized settings and secrets.

## Details

New `parameters` fields have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These fields accept a map of `ConnectorConfigurationParameterValue` objects, which support boolean, double, int32, string, and secret types. Notably, `secretValue` is only permitted within authentication parameters. Developers can update specific parameters by targeting them in the `update_mask` (e.g., `configuration.parameters.my_param_id`), with support for backtick escaping for IDs containing special characters.

**Tags:** `BigQuery` `Connectors` `Authentication` `Secrets`
