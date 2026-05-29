---
date: 2026-05-29
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill IDs"
impact: high
breaking: true
tags: ["ai", "breaking-change", "governance", "agents"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill IDs

**Date:** 2026-05-29  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine while making several breaking changes to Agents, Skills, and GenAI response formats.

## Details

This update introduces the `SemanticGovernancePolicyEngine` singleton and `SemanticGovernancePolicies` resources for location-based policy management. Several breaking changes were introduced: `skillId` is now a required parameter in `skills.create`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `GenaiVertexV1beta1AudioResponseFormat` and `ImageResponseFormat` have renamed their `URL` enum values to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types, including `hyperdisk-balanced`, `hyperdisk-ml`, and `hyperdisk-throughput`.

**Tags:** `ai` `breaking-change` `governance` `agents`
