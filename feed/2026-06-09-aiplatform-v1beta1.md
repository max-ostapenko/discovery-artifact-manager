---
date: 2026-06-09
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives as Agent Platform refactors"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance arrives as Agent Platform refactors

**Date:** 2026-06-09  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 introduces a new Semantic Governance Policy Engine and refactors several Agent-related resources, including multiple breaking enum and parameter changes.

## Details

This update introduces the `SemanticGovernancePolicyEngine`, a singleton resource for managing AI governance states, along with `SemanticGovernancePolicies` for location-based policy management. Developers using the Agent Platform should note significant refactoring: the `interactions` resource has been moved under location-based paths. 

Several breaking changes are included: 
1. In `AudioResponseFormat` and `ImageResponseFormat`, the enum value `URL` has been renamed to `URI`.
2. The `AgentTool` type `mcp` is now `mcp_server`.
3. The `skillId` parameter in `skills.create` has changed from Optional to Required.
4. `PersistentDiskSpec` now supports Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`). 

Additionally, documentation is shifting terminology from 'Vertex AI' to 'Agent Platform' across several resource descriptions.

**Tags:** `AI` `Vertex AI` `Governance` `Breaking Change`
