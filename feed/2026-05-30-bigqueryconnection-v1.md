---
date: 2026-05-30
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible Parameter Support for External Connectors"
impact: medium
breaking: false
tags: ["bigquery", "external-data", "connectivity"]
interesting_score: 6
---

# Flexible Parameter Support for External Connectors

**Date:** 2026-05-30  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both general connector configuration and authentication, enabling more granular control over external data source settings.

## Details

New `parameters` maps have been added to `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize a new `ConnectorConfigurationParameterValue` schema, which supports typed values including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter specifically for authentication). Developers can update individual parameters via `ConnectionService.UpdateConnection` by using a specific `update_mask` path, with support for backtick-escaping parameter IDs that contain special characters.

**Tags:** `bigquery` `external-data` `connectivity`
