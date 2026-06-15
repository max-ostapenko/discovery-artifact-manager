---
date: 2026-06-15
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI v1beta1: Agent Platform Pivot & Breaking Changes"
impact: high
breaking: true
tags: ["agents", "breaking-change", "governance", "generative-ai"]
interesting_score: 9
---

# Vertex AI v1beta1: Agent Platform Pivot & Breaking Changes

**Date:** 2026-06-15  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 surface area reflects a strategic shift toward the 'Agent Platform,' introducing semantic governance and anomaly detection while implementing breaking changes to the Interactions API.

## Details

This update includes several breaking changes: the `interactions.delete` method has been removed, and parameters `include_input` and `last_event_id` in the `getPoll` and `getStream` methods have been renamed to camelCase (`includeInput`, `lastEventId`). New resources include `SemanticGovernancePolicyEngine`, a singleton for policy management, and `AgentAnomalyDetectionScope` for monitoring. The `Agent` resource has been refined, including renaming the `mcp` tool type to `mcp_server`. Additionally, `PersistentDiskSpec` now supports Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and the Google Maps contextual widget is officially deprecated.

**Tags:** `agents` `breaking-change` `governance` `generative-ai`
