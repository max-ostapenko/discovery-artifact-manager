---
date: 2026-06-07
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Agent API Changes"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance and Breaking Agent API Changes

**Date:** 2026-06-07  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance framework while implementing several breaking changes to the Agents and Skills API surfaces, including required IDs and enum renames.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies resources for managing AI governance at the location level. Developers should be aware of several breaking changes: the `skillId` parameter in `projects.locations.skills.create` is now Required (previously Optional), and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, the `URL` enum value in `AudioResponseFormat` and `ImageResponseFormat` has been changed to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
