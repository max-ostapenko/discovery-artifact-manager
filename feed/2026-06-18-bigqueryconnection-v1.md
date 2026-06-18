---
date: 2026-06-18
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible connector parameters for BigQuery Connections"
impact: medium
breaking: false
tags: ["BigQuery", "Data Integration", "Connectors"]
interesting_score: 6
---

# Flexible connector parameters for BigQuery Connections

**Date:** 2026-06-18  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both general connector configurations and authentication settings.

## Details

A new `parameters` map has been added to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize the new `ConnectorConfigurationParameterValue` schema, which supports a variety of types including `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue` (the latter being exclusive to authentication). This change allows developers to pass connector-specific flags that aren't part of the standard API schema. Notably, individual parameters can be targeted during updates using specific `update_mask` paths, and the API now explicitly supports backtick-escaped parameter IDs for keys containing special characters.

**Tags:** `BigQuery` `Data Integration` `Connectors`
