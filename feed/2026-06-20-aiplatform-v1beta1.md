---
date: 2026-06-20
api: aiplatform.v1beta1
service: Vertex AI
title: "Breaking Changes to Agents and New Governance Tools"
impact: high
breaking: true
tags: ["ai", "agents", "breaking-change", "governance"]
interesting_score: 8
---

# Breaking Changes to Agents and New Governance Tools

**Date:** 2026-06-20  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces Semantic Governance and Anomaly Detection for Agents, alongside significant breaking changes to existing Agent and Interaction resource schemas.

## Details

This update includes several breaking changes: the `interactions.delete` method has been removed, and `skillId` is now a required parameter in `skills.create`. Multiple parameters in `getPoll` and `getStream` have shifted from snake_case to camelCase (e.g., `include_input` to `includeInput`). Additionally, the `Agent` list method now uses `created` and `updated` for ordering instead of `create_time` and `update_time`. New capabilities include the `SemanticGovernancePolicyEngine` singleton for policy management and `AgentAnomalyDetectionScope` for monitoring. Developers should also note that `AgentTool` types have changed from `mcp` to `mcp_server`, and several enum values have transitioned from `URL` to `URI`.

**Tags:** `ai` `agents` `breaking-change` `governance`
