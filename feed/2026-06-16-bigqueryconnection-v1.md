---
date: 2026-06-16
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Dynamic parameters added to Connector Configurations"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "configuration"]
interesting_score: 6
---

# Dynamic parameters added to Connector Configurations

**Date:** 2026-06-16  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

BigQuery Connection now supports arbitrary, typed key-value parameters for both general connector settings and authentication blocks.

## Details

The API has introduced a `parameters` map to both `ConnectorConfiguration` and `ConnectorConfigurationAuthentication` schemas. These maps utilize a new `ConnectorConfigurationParameterValue` type, which supports boolean, double, int32, string, and secret values. This change allows developers to pass connector-specific configuration that isn't part of the standard schema. Note that when updating these via `UpdateConnection`, parameter IDs with special characters must be escaped with backticks in the `update_mask`.

**Tags:** `bigquery` `connectors` `configuration`
