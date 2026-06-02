---
date: 2026-06-02
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill creation"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill creation

**Date:** 2026-06-02  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while simultaneously introducing breaking changes to Skill creation and GenAI response formats.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies resources for managing AI governance at the location level. Crucially, several breaking changes are included: the `skillId` parameter in `skills.create` has moved from Optional to Required, and the enum value `URL` has been renamed to `URI` in both `AudioResponseFormat` and `ImageResponseFormat`. Additionally, the `AgentTool` type `mcp` has been renamed to `mcp_server`. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types including `hyperdisk-balanced`, `hyperdisk-extreme`, and `hyperdisk-ml`.

**Tags:** `AI` `Vertex AI` `Governance` `Breaking Change`
