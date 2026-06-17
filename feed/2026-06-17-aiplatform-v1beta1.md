---
date: 2026-06-17
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: New Governance Tools and Breaking Agent Changes"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Agents", "Governance"]
interesting_score: 8
---

# Vertex AI Beta: New Governance Tools and Breaking Agent Changes

**Date:** 2026-06-17  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance and Anomaly Detection for Agents while implementing several breaking changes to the Agent and Interaction APIs, including parameter renames and new required fields.

## Details

Vertex AI has added the `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope` resources for better control over AI agent behavior. However, several breaking changes were introduced: the `interactions.delete` method was removed, and the `skillId` parameter in `skills.create` is now required. Additionally, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and enum values for `AudioResponseFormat` and `ImageResponseFormat` have shifted from `URL` to `URI`. 

Developers should also note the renaming of interaction parameters from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). A massive internal schema refactoring has also renamed generic `GenaiStruct` and `GenaiValue` types to `GenaiVertexV1beta1Struct` and `GenaiVertexV1beta1Value` respectively.

**Tags:** `AI` `Vertex AI` `Agents` `Governance`
