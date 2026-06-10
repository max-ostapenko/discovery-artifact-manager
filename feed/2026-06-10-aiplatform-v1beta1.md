---
date: 2026-06-10
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Governance Engine and Agent Platform Refactor"
impact: high
breaking: true
tags: ["breaking-change", "ai-agents", "governance", "vertex-ai"]
interesting_score: 8
---

# Vertex AI Governance Engine and Agent Platform Refactor

**Date:** 2026-06-10  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance Policy Engine for AI oversight and includes several breaking changes to the Agent and Skill management APIs.

## Details

The v1beta1 surface sees the addition of SemanticGovernancePolicyEngine (a singleton resource) and SemanticGovernancePolicies, enabling structured governance over AI interactions. Significant breaking changes include making `skillId` a required parameter in `skills.create`, renaming the `mcp` tool type to `mcp_server` in `AgentTool`, and moving `interactions.delete` to a location-scoped path. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (balanced, extreme, ML, throughput), and delivery enums for audio/image formats have transitioned from `URL` to `URI` naming.

**Tags:** `breaking-change` `ai-agents` `governance` `vertex-ai`
