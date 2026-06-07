---
date: 2026-06-07
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent Platform Restructuring"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance and Agent Platform Restructuring

**Date:** 2026-06-07  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance framework and restructures the Interactions API, alongside several breaking changes to parameter requirements and enum values.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicy` resources, enabling fine-grained control over AI behaviors. The `interactions` resource has been moved from a top-level path to a location-scoped path under `projects.locations.interactions`. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required, and the `delivery` enum in GenAI response formats has changed from `URL` to `URI`. Additionally, documentation across the API is shifting terminology from 'Vertex AI' to 'Agent Platform' for specific agentic resource types.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
