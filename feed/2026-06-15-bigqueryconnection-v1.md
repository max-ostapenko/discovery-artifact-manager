---
date: 2026-06-15
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible parameters for BigQuery Connections"
impact: medium
breaking: false
tags: ["bigquery", "connectivity", "configuration"]
interesting_score: 6
---

# Flexible parameters for BigQuery Connections

**Date:** 2026-06-15  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both connector and authentication configurations, allowing for non-standard settings and secrets.

## Details

New `parameters` maps have been added to `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize the new `ConnectorConfigurationParameterValue` schema, which supports a variety of data types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (exclusive to authentication). Developers can target specific parameters during updates using the `update_mask` field, and the API now supports backtick escaping for parameter IDs that contain special characters.

**Tags:** `bigquery` `connectivity` `configuration`
