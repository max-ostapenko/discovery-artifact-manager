---
date: 2026-06-18
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes to Agents and New Governance"
impact: high
breaking: true
tags: ["agents", "genai", "breaking-change", "governance"]
interesting_score: 9
---

# Vertex AI Beta: Breaking Changes to Agents and New Governance

**Date:** 2026-06-18  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces the Semantic Governance Policy Engine and Agent Anomaly Detection, while applying several breaking changes to the Agents and Skills APIs, including parameter renames and new required fields.

## Details

Several breaking changes have been introduced: the `skillId` parameter in `skills.create` is now required, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. In the `interactions` resource, snake_case parameters like `include_input` and `last_event_id` have been replaced with camelCase versions (`includeInput`, `lastEventId`), and the `interactions.delete` method has been removed. On the feature side, a new singleton resource `SemanticGovernancePolicyEngine` is now available for retrieval and upsert, and `AgentAnomalyDetectionScope` has been added. Additionally, the API has undergone a massive internal schema refactoring, renaming many `Genai*` types to `GenaiVertexV1beta1*` (e.g., `GenaiStruct` is now `GenaiVertexV1beta1Struct`).

**Tags:** `agents` `genai` `breaking-change` `governance`
