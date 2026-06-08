---
date: 2026-06-08
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and refines Agent Platform"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and refines Agent Platform

**Date:** 2026-06-08  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and makes several breaking changes to the Agent and Skill APIs, including renaming tool types and making IDs required.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicy` resources, enabling structured governance over AI interactions. Several breaking changes were introduced in the Agent Platform components: the `skillId` is now a required parameter for creating Skills, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, the `interactions` resource has been moved under the `projects.locations` hierarchy, and the `AudioResponseFormat` and `ImageResponseFormat` schemas have changed their delivery enum from `URL` to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
