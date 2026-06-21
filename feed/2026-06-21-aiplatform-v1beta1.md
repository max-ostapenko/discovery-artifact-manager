---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent API Refactoring"
impact: high
breaking: true
tags: ["agents", "governance", "breaking-change"]
interesting_score: 9
---

# Semantic Governance and Agent API Refactoring

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and Agent Anomaly Detection, alongside breaking changes to Agent tool types and required parameters.

## Details

This update introduces the `SemanticGovernancePolicyEngine`, a singleton resource for managing AI governance policies at the location level. It also adds `AgentAnomalyDetectionScope` for monitoring agentic workflows. Significant refactoring has occurred in the Agents surface: the `AgentTool` type `mcp` is now `mcp_server`, and several GenAI-related schemas have been renamed (e.g., `GenaiStruct` to `GenaiVertexV1beta1Struct`). Additionally, the `interactions.delete` method has been removed, and polling/streaming parameters have transitioned from snake_case to camelCase (e.g., `last_event_id` to `lastEventId`).

**Tags:** `agents` `governance` `breaking-change`
