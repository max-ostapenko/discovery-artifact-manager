---
date: 2026-06-06
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent Platform Refinements"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Agents"]
interesting_score: 8
---

# Semantic Governance and Agent Platform Refinements

**Date:** 2026-06-06  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance resources, restructures Agent Platform interactions, and implements several breaking changes to Skill creation and response formats.

## Details

Vertex AI has added a new `SemanticGovernancePolicyEngine` singleton and `SemanticGovernancePolicies` resource for managing AI governance at the location level. The `Interactions` resource has been moved under the `projects.locations` hierarchy. Crucially, `skillId` is now a required parameter in `skills.create`, and the default `pageSize` for listing agents has dropped from 100 to 10. Additionally, `AudioResponseFormat` and `ImageResponseFormat` have renamed the `URL` enum value to `URI`, and the `AgentTool` type `mcp` is now `mcp_server`. New support for various Hyperdisk types (e.g., `hyperdisk-balanced`, `hyperdisk-ml`) has also been added to `PersistentDiskSpec`.

**Tags:** `AI` `Vertex AI` `Governance` `Agents`
