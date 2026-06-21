---
date: 2026-06-21
api: bigqueryconnection.v1
service: BigQuery Connection API
title: "Flexible connector-specific parameters added"
impact: medium
breaking: false
tags: ["bigquery", "configuration", "connectors"]
interesting_score: 6
---

# Flexible connector-specific parameters added

**Date:** 2026-06-21  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary, typed key-value parameters for both general connector and authentication configurations.

## Details

New `parameters` fields have been added to the `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps allow developers to pass connector-specific settings that aren't part of the standard schema using the new `ConnectorConfigurationParameterValue` type, which supports `boolValue`, `doubleValue`, `int32Value`, `stringValue`, and `secretValue`. The update also introduces specific guidance on using `update_mask` for these parameters and escaping non-standard parameter IDs with backticks.

**Tags:** `bigquery` `configuration` `connectors`
