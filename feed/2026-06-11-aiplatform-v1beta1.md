---
date: 2026-06-11
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and refines Agent Platform"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change", "Infrastructure"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and refines Agent Platform

**Date:** 2026-06-11  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine and significantly updates the Agent Platform, including breaking changes to resource paths and required parameters.

## Details

This update introduces a suite of 'Semantic Governance' resources, including a singleton `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` for fine-grained AI control. The Agent Platform is maturing, with documentation shifting terminology from 'Vertex AI' to 'Agent Platform' and the `AgentTool` type `mcp` being renamed to `mcp_server`. Developers should note several breaking changes: `skillId` is now required for creating skills, the `interactions.delete` method has been moved under the `projects.locations` hierarchy, and `URL` enum values in `AudioResponseFormat` and `ImageResponseFormat` have been renamed to `URI`. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-extreme`) for high-performance I/O.

**Tags:** `AI` `Governance` `Agents` `Breaking Change` `Infrastructure`
