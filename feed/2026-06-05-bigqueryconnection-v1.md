---
date: 2026-06-05
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameters added to Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "ExternalData", "Configuration"]
interesting_score: 6
---

# Flexible parameters added to Connector Configurations

**Date:** 2026-06-05  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for both general connector settings and authentication, enabling more granular and extensible configurations.

## Details

The `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas have been updated with a new `parameters` field. This field accepts a map of `ConnectorConfigurationParameterValue` objects, which can store boolean, double, int32, string, or secret values. This allows developers to pass connector-specific settings that aren't part of the standard schema. Additionally, individual parameters can be targeted for updates using the `update_mask` in the `UpdateConnection` method, including support for backtick-escaping parameter IDs with special characters.

**Tags:** `BigQuery` `ExternalData` `Configuration`
