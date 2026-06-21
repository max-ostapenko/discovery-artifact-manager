---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Agent Changes & New Governance Tools"
impact: high
breaking: true
tags: ["agents", "generative-ai", "breaking-change", "governance"]
interesting_score: 9
---

# Vertex AI Beta: Breaking Agent Changes & New Governance Tools

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Significant updates to the AI Platform v1beta1 API include the introduction of Semantic Governance and Anomaly Detection for agents, alongside several breaking changes to parameter naming and required fields.

## Details

This update introduces the `SemanticGovernancePolicyEngine` (a singleton resource for policy management) and `AgentAnomalyDetectionScope` for monitoring agent behavior. However, developers must address several breaking changes: the `interactions.delete` method has been removed, and parameters in `getPoll` and `getStream` have shifted from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). Additionally, `skillId` is now a required parameter in `skills.create`, and several schema references have been renamed (e.g., `GenaiStruct` is now `GenaiVertexV1beta1Struct`).

**Tags:** `agents` `generative-ai` `breaking-change` `governance`
