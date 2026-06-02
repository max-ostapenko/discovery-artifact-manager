---
date: 2026-06-02
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI introduces Semantic Governance and breaking GenAI changes"
impact: high
breaking: true
tags: ["governance", "genai", "breaking-change", "agents"]
interesting_score: 8
---

# Vertex AI introduces Semantic Governance and breaking GenAI changes

**Date:** 2026-06-02  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework while delivering several breaking changes to GenAI response formats, Agent tool types, and Skill creation requirements.

## Details

Vertex AI has added a new governance layer with `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicy` resources, allowing for structured policy management at the location level. However, developers should be wary of several breaking changes: the `GenaiVertexV1beta1AudioResponseFormat` and `ImageResponseFormat` enums have renamed `URL` to `URI`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `skills.create` now requires a `skillId` parameter which was previously optional. On the infrastructure side, `PersistentDiskSpec` has been expanded to support various Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-extreme`.

**Tags:** `governance` `genai` `breaking-change` `agents`
