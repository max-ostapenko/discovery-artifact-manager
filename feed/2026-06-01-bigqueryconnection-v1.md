---
date: 2026-06-01
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Custom parameters for BigQuery connector configurations"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Custom parameters for BigQuery connector configurations

**Date:** 2026-06-01  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both general connector configuration and authentication.

## Details

Developers can now pass non-standardized configuration settings through the new `parameters` map in `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. This is powered by a new `ConnectorConfigurationParameterValue` schema that supports typed values including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and a `secretValue` (reserved for authentication). Updates to these parameters can be targeted specifically using an `update_mask` in the `UpdateConnection` method, with support for backtick-escaped parameter IDs.

**Tags:** `bigquery` `connectors` `configuration`
