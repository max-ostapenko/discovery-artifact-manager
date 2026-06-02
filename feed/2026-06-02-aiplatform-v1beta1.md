---
date: 2026-06-02
api: aiplatform.v1beta1
service: Vertex AI
title: "New Semantic Governance and Breaking Changes to Skills"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "infrastructure"]
interesting_score: 8
---

# New Semantic Governance and Breaking Changes to Skills

**Date:** 2026-06-02  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a Semantic Governance Policy Engine and associated policies, while introducing breaking changes to Skill creation and Agent tool definitions.

## Details

This update introduces the `SemanticGovernancePolicyEngine` (a singleton resource) and `SemanticGovernancePolicies` for managing AI governance at the location level. Crucially, there are several breaking changes: the `skillId` parameter in `projects.locations.skills.create` is now 'Required' (previously 'Optional'), and the `steps` field in `GenaiVertexV1beta1Interaction` is now marked as 'Required'. Additionally, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and response formats for audio and images have transitioned from `URL` to `URI` terminology. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `governance` `agents` `breaking-change` `infrastructure`
