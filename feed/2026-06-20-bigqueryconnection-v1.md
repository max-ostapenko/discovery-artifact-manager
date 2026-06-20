---
date: 2026-06-20
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible typed parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Data Connectors", "Configuration"]
interesting_score: 6
---

# Flexible typed parameters for Connector Configurations

**Date:** 2026-06-20  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary, typed key-value pairs for connector and authentication configurations, enabling support for non-standard connector settings.

## Details

The API has introduced a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type, which supports boolean, double, int32, string, and secret values. This allows developers to pass connector-specific configuration that isn't part of the standard schema. Additionally, the API now supports granular updates to these parameters via `update_mask` in the `UpdateConnection` method, including a specific backtick-escaping syntax for parameter IDs that contain special characters.

**Tags:** `BigQuery` `Data Connectors` `Configuration`
