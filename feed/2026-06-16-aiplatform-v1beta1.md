---
date: 2026-06-16
api: aiplatform.v1beta1
service: Vertex AI / Agent Platform
title: "Vertex AI v1beta1: Breaking Renames and Agent Platform Pivot"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "infrastructure"]
interesting_score: 9
---

# Vertex AI v1beta1: Breaking Renames and Agent Platform Pivot

**Date:** 2026-06-16  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the AI Platform beta introduces several breaking changes to interactions and tools, while signaling a major strategic shift toward a dedicated 'Agent Platform.'

## Details

This update includes significant breaking changes: the `interactions.delete` method has been removed, and parameters for `getPoll` and `getStream` have been renamed from snake_case to camelCase (e.g., `last_event_id` is now `lastEventId`). Additionally, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and `skillId` is now a required field when creating a Skill. 

On the feature side, a new singleton resource `SemanticGovernancePolicyEngine` has been introduced for policy management, alongside `AgentAnomalyDetectionScope` for monitoring. Infrastructure-wise, `PersistentDiskSpec` now supports a wide array of Hyperdisk types (balanced, extreme, ML, and throughput). Developers should also note the extensive documentation updates where 'Vertex AI' is being rebranded as 'Agent Platform' or 'Gemini Enterprise Agent Platform' across many resource descriptions.

**Tags:** `breaking-change` `agents` `governance` `infrastructure`
