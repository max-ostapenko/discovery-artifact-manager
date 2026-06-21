---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes and New Governance Tools"
impact: high
breaking: true
tags: ["AI", "VertexAI", "BreakingChange", "Governance"]
interesting_score: 9
---

# Vertex AI Beta: Breaking Changes and New Governance Tools

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 surface introduces the Semantic Governance Policy Engine and Agent Anomaly Detection while enforcing stricter schema requirements and renaming several parameters.

## Details

This update includes significant breaking changes: the `interactions.delete` method has been removed, and several query parameters in `getPoll` and `getStream` have transitioned from snake_case to camelCase (e.g., `include_input` is now `includeInput`). Developers should also note that `skillId` and `Interaction.steps` are now required fields. On the feature side, a new singleton resource `SemanticGovernancePolicyEngine` has been added for policy management, alongside `AgentAnomalyDetectionScope` for monitoring. Additionally, many internal schema references have been namespaced (e.g., `GenaiStruct` to `GenaiVertexV1beta1Struct`) and enum values for audio/image delivery have shifted from `URL` to `URI`.

**Tags:** `AI` `VertexAI` `BreakingChange` `Governance`
