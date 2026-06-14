---
date: 2026-06-14
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent Platform Shift & Breaking Changes"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "storage"]
interesting_score: 9
---

# Vertex AI Beta: Agent Platform Shift & Breaking Changes

**Date:** 2026-06-14  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 surface introduces the 'Agent Platform' branding, adds Semantic Governance and Anomaly Detection, and enforces several breaking parameter renames and requirement changes.

## Details

This update includes significant breaking changes: the `interactions.delete` method has been removed, and several query parameters in `getPoll` and `getStream` have been renamed from snake_case to camelCase (e.g., `include_input` is now `includeInput`). Additionally, `skillId` is now a required parameter for Skill creation, and the `mcp` tool type has been renamed to `mcp_server`. On the feature side, a new `SemanticGovernancePolicyEngine` singleton resource and `AgentAnomalyDetectionScopes` have been introduced. The `PersistentDiskSpec` now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`. Developers should also note a documentation shift where 'Vertex AI' is being rebranded as 'Agent Platform' in several resource descriptions.

**Tags:** `breaking-change` `agents` `governance` `storage`
