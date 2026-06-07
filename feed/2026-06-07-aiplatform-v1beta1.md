---
date: 2026-06-07
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and the shift to Agent Platform"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance and the shift to Agent Platform

**Date:** 2026-06-07  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance framework and undergoes a significant terminology shift toward 'Agent Platform', accompanied by several breaking changes to enums and required fields.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicy resources, enabling fine-grained control over AI behavior. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required, and the `mcp` tool type for Agents has been renamed to `mcp_server`. Additionally, the `URL` enum value in Audio and Image response formats has been changed to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
