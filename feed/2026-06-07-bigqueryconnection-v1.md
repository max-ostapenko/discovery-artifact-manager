---
date: 2026-06-07
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Dynamic parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "API Update"]
interesting_score: 6
---

# Dynamic parameters for Connector Configurations

**Date:** 2026-06-07  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary, connector-specific parameters for both general configuration and authentication blocks.

## Details

New `parameters` maps have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps allow for name-value pairs using the new `ConnectorConfigurationParameterValue` type, which supports a variety of scalars (bool, double, int32, string) and secrets. Developers can perform granular updates on these parameters using the `update_mask` in `ConnectionService.UpdateConnection`, including support for escaping non-standard parameter IDs with backticks.

**Tags:** `BigQuery` `Data Integration` `API Update`
