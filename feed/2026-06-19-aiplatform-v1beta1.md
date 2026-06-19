---
date: 2026-06-19
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent Anomaly Detection"
impact: high
breaking: true
tags: ["genai", "agents", "governance", "breaking-change"]
interesting_score: 8
---

# Semantic Governance and Agent Anomaly Detection

**Date:** 2026-06-19  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces Semantic Governance Policy Engines and Agent Anomaly Detection Scopes alongside significant refactoring of GenAI schemas and tool types.

## Details

This update adds management methods for `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope`. Developers can now resume interaction streams using the new `lastEventId` parameter in `getPoll` and `getStream`. Several breaking changes are included: the `interactions.delete` method was removed, `skillId` is now a required parameter for `skills.create`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, many internal GenAI schemas were renamed (e.g., `GenaiStruct` to `GenaiVertexV1beta1Struct`), and `URL` enums were changed to `URI` for audio and image response formats.

**Tags:** `genai` `agents` `governance` `breaking-change`
