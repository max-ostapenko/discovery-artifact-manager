---
date: 2026-05-30
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives as Skill IDs become required"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "storage"]
interesting_score: 8
---

# Semantic Governance arrives as Skill IDs become required

**Date:** 2026-05-30  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while implementing several breaking changes to Skills, Agents, and GenAI response formats.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing location-based governance, alongside a new SemanticGovernancePolicies resource. Significant breaking changes include making 'skillId' a required parameter in 'skills.create' and renaming the 'mcp' tool type to 'mcp_server' in 'AgentTool'. Additionally, 'GenaiVertexV1beta1' response formats for Audio and Image have transitioned the 'URL' enum value to 'URI'. On the infrastructure side, 'PersistentDiskSpec' now supports a wide array of Hyperdisk types including 'hyperdisk-balanced', 'hyperdisk-ml', and 'hyperdisk-throughput'.

**Tags:** `governance` `agents` `breaking-change` `storage`
