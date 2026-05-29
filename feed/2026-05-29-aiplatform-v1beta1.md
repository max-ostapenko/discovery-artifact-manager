---
date: 2026-05-29
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and refines Agent tools"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and refines Agent tools

**Date:** 2026-05-29  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and associated policies, while also implementing breaking changes to Agent tool types and Skill creation requirements.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI governance at the location level, along with a new SemanticGovernancePolicies resource for granular control. Developers using Vertex AI Agents should note a breaking change: the `AgentTool.type` enum value 'mcp' has been renamed to 'mcp_server'. Additionally, the `skillId` parameter in the `skills.create` method is now marked as Required. On the infrastructure side, PersistentDiskSpec now supports a wide array of Hyperdisk options, including hyperdisk-balanced, hyperdisk-extreme, hyperdisk-ml, and hyperdisk-throughput.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
