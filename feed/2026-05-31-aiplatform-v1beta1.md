---
date: 2026-05-31
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives as Skill IDs become required"
impact: high
breaking: true
tags: ["governance", "genai", "breaking-change", "infrastructure"]
interesting_score: 8
---

# Semantic Governance arrives as Skill IDs become required

**Date:** 2026-05-31  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while implementing breaking changes to Skill creation and GenAI response formats.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI governance policies, alongside a new SemanticGovernancePolicies resource. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required rather than optional, and the `delivery` enum in GenAI Audio/Image response formats has changed from `URL` to `URI`. Additionally, the `AgentTool` type `mcp` has been renamed to `mcp_server`. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types, including `hyperdisk-balanced`, `hyperdisk-extreme`, and `hyperdisk-ml`.

**Tags:** `governance` `genai` `breaking-change` `infrastructure`
