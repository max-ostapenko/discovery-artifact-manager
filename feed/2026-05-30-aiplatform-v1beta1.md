---
date: 2026-05-30
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill creation"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill creation

**Date:** 2026-05-30  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the AI Platform beta API introduces Semantic Governance Policies while enforcing stricter requirements for Skill creation and Agent Tooling.

## Details

This update introduces a new Semantic Governance framework, including the `SemanticGovernancePolicyEngine` singleton and `SemanticGovernancePolicy` resources for location-based AI oversight. Crucially, several breaking changes were introduced: the `skillId` parameter in `projects.locations.skills.create` is now required rather than optional, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `GenaiVertexV1beta1AudioResponseFormat` and `ImageResponseFormat` have transitioned from `URL` to `URI` in their delivery enums. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `AI` `Vertex AI` `Governance` `Breaking Change`
