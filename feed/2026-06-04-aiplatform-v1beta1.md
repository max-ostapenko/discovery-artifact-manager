---
date: 2026-06-04
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and refines Agents"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and refines Agents

**Date:** 2026-06-04  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and associated policies, while making breaking changes to Agent tool types and Skill creation requirements.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources for managing AI governance at the location level. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `PersistentDiskSpec` has been expanded to support multiple Hyperdisk types (balanced, extreme, ML, and throughput), and GenAI response formats for audio and images have transitioned from 'URL' to 'URI' terminology.

**Tags:** `AI` `Vertex AI` `Governance` `Agents` `Breaking Change`
