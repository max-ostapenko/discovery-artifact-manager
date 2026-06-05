---
date: 2026-06-05
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill IDs"
impact: high
breaking: true
tags: ["Vertex AI", "AI Governance", "Breaking Change", "Agents"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill IDs

**Date:** 2026-06-05  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while implementing several breaking changes to Skills, Agents, and response formats.

## Details

This update introduces the Semantic Governance Policy Engine, a singleton resource for managing AI governance policies via `getSemanticGovernancePolicyEngine` and `updateSemanticGovernancePolicyEngine`. Crucially, several breaking changes have been introduced: the `skillId` parameter in `skills.create` is now Required rather than Optional, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `AudioResponseFormat` and `ImageResponseFormat` have transitioned their delivery enums from `URL` to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `Vertex AI` `AI Governance` `Breaking Change` `Agents`
