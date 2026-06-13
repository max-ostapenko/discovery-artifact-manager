---
date: 2026-06-13
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Changes for Agents"
impact: high
breaking: true
tags: ["Vertex AI", "Generative AI", "Governance", "Breaking Change"]
interesting_score: 9
---

# Semantic Governance and Breaking Changes for Agents

**Date:** 2026-06-13  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and makes several breaking changes to the Agents and GenAI API surfaces, including required IDs and renamed enum values.

## Details

This update introduces the Semantic Governance Policy Engine, a singleton resource for managing AI governance policies at the location level. Significant breaking changes include making `skillId` a required parameter in `skills.create` and renaming the `mcp` tool type to `mcp_server` in `AgentTool`. Additionally, the GenAI response formats for audio and images have transitioned from `URL` to `URI` enum values, which will break existing code relying on the old string constants. The `interactions` resource has also been moved under the standard `projects.locations` hierarchy, and `PersistentDiskSpec` now supports several new Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `Vertex AI` `Generative AI` `Governance` `Breaking Change`
