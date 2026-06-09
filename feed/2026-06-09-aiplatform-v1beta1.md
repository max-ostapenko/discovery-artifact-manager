---
date: 2026-06-09
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Agent schemas"
impact: high
breaking: true
tags: ["AI", "Governance", "Breaking Change", "Agents"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Agent schemas

**Date:** 2026-06-09  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and associated policies while implementing several breaking changes to the Agents and Skills API surface.

## Details

This update introduces the `SemanticGovernancePolicyEngine` (a singleton resource) and `SemanticGovernancePolicies` for managing AI behavior. Significant breaking changes include: the `skillId` is now required when creating Skills; the `AgentTool` type `mcp` has been renamed to `mcp_server`; and the `URL` enum value in `AudioResponseFormat` and `ImageResponseFormat` has been changed to `URI`. Additionally, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), and the `interactions.delete` method has been moved to a location-nested path.

**Tags:** `AI` `Governance` `Breaking Change` `Agents`
