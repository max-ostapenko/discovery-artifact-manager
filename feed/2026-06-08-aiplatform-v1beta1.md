---
date: 2026-06-08
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives as Agent Platform rebrands"
impact: high
breaking: true
tags: ["breaking-change", "genai", "agents", "governance"]
interesting_score: 8
---

# Semantic Governance arrives as Agent Platform rebrands

**Date:** 2026-06-08  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework and makes several breaking changes to the GenAI and Agent APIs, including enum renames and resource path restructuring.

## Details

Vertex AI is introducing a Semantic Governance framework via the new `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, allowing for structured policy management. Several breaking changes are included: the `GenaiVertexV1beta1AudioResponseFormat` and `ImageResponseFormat` enums have changed `URL` to `URI`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `skillId` is now a required parameter for `skills.create`, and the `interactions` resource has been moved under the `projects.locations` hierarchy. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `breaking-change` `genai` `agents` `governance`
