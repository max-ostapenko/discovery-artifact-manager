---
date: 2026-06-17
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI v1beta1: Breaking Changes and Agent Platform Shift"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "infrastructure"]
interesting_score: 8
---

# Vertex AI v1beta1: Breaking Changes and Agent Platform Shift

**Date:** 2026-06-17  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A significant update to the AI Platform v1beta1 API introduces new governance resources while implementing several breaking changes to parameter naming, enum values, and resource requirements.

## Details

This update introduces the `SemanticGovernancePolicyEngine` (a singleton resource for policy management) and `AgentAnomalyDetectionScopes`. However, developers should be wary of several breaking changes: the `interactions.delete` method has been removed, and the `skillId` parameter in `skills.create` is now Required rather than Optional. Additionally, multiple fields have been renamed for consistency: `AgentTool` types changed from `mcp` to `mcp_server`, and response formats for audio/image delivery changed from `URL` to `URI`. Query parameters for interaction polling and streaming have also shifted from snake_case to camelCase (e.g., `include_input` to `includeInput`). On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `breaking-change` `agents` `governance` `infrastructure`
