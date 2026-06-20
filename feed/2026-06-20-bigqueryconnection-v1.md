---
date: 2026-06-20
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible key-value parameters for connector configurations"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Flexible key-value parameters for connector configurations

**Date:** 2026-06-20  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both general connector settings and authentication, providing an extensible way to configure external data sources.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type, which supports a variety of data types including boolean, double, int32, string, and a specialized `secretValue` for sensitive authentication data. Developers can update specific parameters individually via `ConnectionService.UpdateConnection` by targeting the `update_mask` at specific keys, such as `configuration.parameters.my_param_id`.

**Tags:** `bigquery` `connectors` `configuration`
