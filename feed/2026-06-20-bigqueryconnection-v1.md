---
date: 2026-06-20
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible custom parameters for BigQuery Connectors"
impact: medium
breaking: false
tags: ["BigQuery", "Connectors", "API Update"]
interesting_score: 6
---

# Flexible custom parameters for BigQuery Connectors

**Date:** 2026-06-20  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection API now supports arbitrary key-value parameters for connector configuration and authentication, allowing for more granular control over specialized data sources.

## Details

New `parameters` maps have been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps use the new `ConnectorConfigurationParameterValue` schema, which supports typed values including booleans, doubles, integers, strings, and secrets. Developers can update individual parameters using the `update_mask` in `UpdateConnection`, with support for backtick-escaped parameter IDs for keys that don't fit standard naming patterns.

**Tags:** `BigQuery` `Connectors` `API Update`
