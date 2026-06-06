---
date: 2026-06-06
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Changes in Agent Tools"
impact: high
breaking: true
tags: ["Vertex AI", "Generative AI", "Governance", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance and Breaking Changes in Agent Tools

**Date:** 2026-06-06  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 introduces a new Semantic Governance framework while delivering several breaking changes to Agent tools, response formats, and Skill creation.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies, allowing for structured governance over AI behaviors. Developers should note several breaking changes: the `skillId` is now required for Skill creation, and the AgentTool type `mcp` has been renamed to `mcp_server`. Additionally, the `URL` enum value in Audio and Image response formats has been changed to `URI`. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`. The `interactions.delete` method has also been moved to a location-scoped path.

**Tags:** `Vertex AI` `Generative AI` `Governance` `Breaking Change`
