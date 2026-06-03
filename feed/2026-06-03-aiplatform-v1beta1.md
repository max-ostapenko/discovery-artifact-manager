---
date: 2026-06-03
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill IDs"
impact: high
breaking: true
tags: ["Vertex AI", "Generative AI", "Governance", "Agents"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill IDs

**Date:** 2026-06-03  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine for managing AI guardrails while landing several breaking changes to Agents and Skills.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, allowing developers to programmatically manage AI governance rules. However, several breaking changes have been introduced: `skills.create` now requires a `skillId`, `Interaction.steps` is now a required field, and `AgentTool` has renamed the `mcp` type to `mcp_server`. Additionally, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `Vertex AI` `Generative AI` `Governance` `Agents`
