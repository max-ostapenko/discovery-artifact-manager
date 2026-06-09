---
date: 2026-06-09
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Agent Platform updates"
impact: high
breaking: true
tags: ["AI", "Governance", "Breaking Change", "Agents"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and Agent Platform updates

**Date:** 2026-06-09  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a Semantic Governance Policy Engine and makes several breaking changes to Agent tools, GenAI response formats, and Skill creation.

## Details

This update introduces a new Semantic Governance Policy Engine, a singleton resource for managing AI policies via `getSemanticGovernancePolicyEngine` and `updateSemanticGovernancePolicyEngine`. Several breaking changes are included: the `URL` enum value in GenAI audio and image response formats has been renamed to `URI`, and the `mcp` tool type in `AgentTool` is now `mcp_server`. Additionally, `skillId` is now a required parameter for creating Skills. On the infrastructure side, `PersistentDiskSpec` now supports Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`. Note the significant documentation shift rebranding several components from 'Vertex AI' to 'Agent Platform'.

**Tags:** `AI` `Governance` `Breaking Change` `Agents`
