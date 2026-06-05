---
date: 2026-06-05
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill IDs"
impact: high
breaking: true
tags: ["AI", "Governance", "Breaking Change", "Infrastructure"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill IDs

**Date:** 2026-06-05  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while introducing several breaking changes to Skills, Agent tools, and GenAI response formats.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicy` resources, enabling structured policy management within AI workflows. However, there are multiple breaking changes: `skills.create` now requires a `skillId` (previously optional), and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, the `GenaiVertexV1beta1` response formats for images and audio have changed their delivery enum values from `URL` to `URI`. On the infrastructure side, `PersistentDiskSpec` has been expanded to support several Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `AI` `Governance` `Breaking Change` `Infrastructure`
