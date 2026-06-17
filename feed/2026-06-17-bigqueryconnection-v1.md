---
date: 2026-06-17
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible key-value parameters for connector configurations"
impact: medium
breaking: false
tags: ["bigquery", "data-integration", "configuration"]
interesting_score: 6
---

# Flexible key-value parameters for connector configurations

**Date:** 2026-06-17  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for both general connector settings and authentication, allowing for more granular, non-standard configurations.

## Details

The API has introduced a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type, which supports boolean, double, int32, string, and secret values. This change allows developers to pass connector-specific settings that aren't part of the standard schema. Notably, specific parameters can be updated individually using the `update_mask` (e.g., `configuration.parameters.parameter_id`), and parameter IDs with special characters must be escaped with backticks.

**Tags:** `bigquery` `data-integration` `configuration`
