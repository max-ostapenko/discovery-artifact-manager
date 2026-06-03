---
date: 2026-06-03
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Hyperdisk support"
impact: high
breaking: true
tags: ["AI", "Governance", "Storage", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and Hyperdisk support

**Date:** 2026-06-03  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance resources for policy management and expands storage options with Hyperdisk support, alongside several breaking changes to Skills and Agent tools.

## Details

Vertex AI has introduced a new Semantic Governance framework, including the `SemanticGovernancePolicyEngine` singleton and `SemanticGovernancePolicies` resource for managing AI policies at the location level. Storage capabilities are expanded in `PersistentDiskSpec` to include Hyperdisk types like `hyperdisk-balanced`, `hyperdisk-ml`, and `hyperdisk-throughput`. 

Several breaking changes were introduced: `skills.create` now requires a `skillId` instead of it being optional. In `AgentTool`, the `mcp` type has been renamed to `mcp_server`. Additionally, `GenaiVertexV1beta1` response formats for audio and images have transitioned the `URL` enum value to `URI`. Developers using Reasoning Engine memories should also note that `scope` and `memory_type` fields are now explicitly marked as immutable during updates.

**Tags:** `AI` `Governance` `Storage` `Breaking Change`
