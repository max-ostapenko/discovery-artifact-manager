---
date: 2026-06-04
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill IDs"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "infrastructure"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill IDs

**Date:** 2026-06-04  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine for enterprise AI management, alongside several breaking changes to Skill creation and Agent tool enums.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies resources, enabling structured policy management within locations. However, developers should note several breaking changes: the `skillId` parameter in `projects.locations.skills.create` is now required rather than optional. Additionally, enum values in `GenaiVertexV1beta1AudioResponseFormat` and `ImageResponseFormat` have been renamed from `URL` to `URI`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `governance` `agents` `breaking-change` `infrastructure`
