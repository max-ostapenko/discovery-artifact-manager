---
date: 2026-06-18
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes to Agents and Governance"
impact: high
breaking: true
tags: ["AI", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI Beta: Breaking Changes to Agents and Governance

**Date:** 2026-06-18  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance and Anomaly Detection for Agents while applying several breaking changes to the Interaction and Skill APIs, including parameter renaming and field requirement updates.

## Details

The Agentic AI surface area sees significant churn. A new singleton resource, `SemanticGovernancePolicyEngine`, and `AgentAnomalyDetectionScope` have been added. However, several breaking changes are present: the `interactions.delete` method has been removed, and the `skillId` parameter in `skills.create` is now 'Required' instead of 'Optional'. Additionally, parameters in `interactions.getPoll` and `interactions.getStream` have been renamed from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). In the `AgentTool` schema, the tool type `mcp` has been renamed to `mcp_server`, and several response formats have shifted from using 'URL' to 'URI' terminology.

**Tags:** `AI` `Agents` `Breaking Change`
