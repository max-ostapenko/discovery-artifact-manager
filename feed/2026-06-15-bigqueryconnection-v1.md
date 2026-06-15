---
date: 2026-06-15
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Custom Parameters for Connector Configurations"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "Connectors"]
interesting_score: 7
---

# Custom Parameters for Connector Configurations

**Date:** 2026-06-15  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for both general connector and authentication configurations.

## Details

The API introduces a flexible `parameters` map to `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps use the new `ConnectorConfigurationParameterValue` schema, allowing developers to pass typed values including booleans, doubles, integers, strings, and secrets (secrets are restricted to authentication blocks). This change enables support for connector-specific settings that fall outside the standard configuration schema.

**Tags:** `BigQuery` `Data Integration` `Connectors`
