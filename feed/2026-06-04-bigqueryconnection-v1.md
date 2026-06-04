---
date: 2026-06-04
api: bigqueryconnection.v1
service: BigQuery Connection
title: "Flexible parameter support for BigQuery Connections"
impact: medium
breaking: false
tags: ["bigquery", "connectors", "authentication"]
interesting_score: 6
---

# Flexible parameter support for BigQuery Connections

**Date:** 2026-06-04  
**API:** `bigqueryconnection.v1`  
**Impact:** Medium  

## Summary

The BigQuery Connection API now supports arbitrary key-value parameters for both connector and authentication configurations.

## Details

New `parameters` maps have been added to `ConnectorConfiguration` and `ConnectorConfigurationAuthentication`. These maps utilize a new `ConnectorConfigurationParameterValue` schema, allowing developers to pass typed values—including booleans, doubles, integers, strings, and secrets—to connectors. This is particularly useful for configuring non-standard connector settings or specific authentication requirements that aren't covered by the base schema. Note that `secretValue` is specifically restricted to authentication parameters.

**Tags:** `bigquery` `connectors` `authentication`
