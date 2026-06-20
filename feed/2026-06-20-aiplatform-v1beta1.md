---
date: 2026-06-20
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes to Agents and Governance"
impact: high
breaking: true
tags: ["agents", "genai", "breaking-change", "governance"]
interesting_score: 8
---

# Vertex AI Beta: Breaking Changes to Agents and Governance

**Date:** 2026-06-20  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance and Anomaly Detection while applying several breaking changes to the Agents and Interactions API surfaces, including parameter renames and required field updates.

## Details

Several breaking changes have landed in the v1beta1 surface. Most notably, `skillId` is now a required parameter when creating a Skill, and the `interactions.delete` method has been removed entirely. Developers using the Agents API should note that `AgentTool` types have changed from `mcp` to `mcp_server`, and various enums have shifted from `URL` to `URI`. 

On the feature side, a new `SemanticGovernancePolicyEngine` singleton resource has been added for policy management, alongside `AgentAnomalyDetectionScope` for monitoring agent behavior. Additionally, interaction streaming methods (`getPoll`, `getStream`) now support a `lastEventId` parameter, allowing clients to resume streams from a specific event chunk.

**Tags:** `agents` `genai` `breaking-change` `governance`
