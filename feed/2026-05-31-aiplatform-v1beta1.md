---
date: 2026-05-31
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes and Semantic Governance"
impact: high
breaking: true
tags: ["AI", "Governance", "Breaking Change", "GenAI"]
interesting_score: 9
---

# Vertex AI Beta: Breaking Changes and Semantic Governance

**Date:** 2026-05-31  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework while landing several breaking changes to Skills, Agent Tools, and GenAI response formats.

## Details

Vertex AI has introduced a Semantic Governance framework, including the `SemanticGovernancePolicyEngine` (a singleton resource supporting upsert via PATCH) and `SemanticGovernancePolicies`. Several breaking changes have been introduced: the `skillId` is now required for Skill creation, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and GenAI response formats for Audio and Image have transitioned the `URL` enum value to `URI`. Additionally, `Interaction.steps` is now a required field. On the infrastructure side, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `AI` `Governance` `Breaking Change` `GenAI`
