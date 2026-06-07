---
date: 2026-06-07
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent Platform Refactor"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 9
---

# Semantic Governance and Agent Platform Refactor

**Date:** 2026-06-07  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework and significant breaking changes to the Agent Platform, including resource path migrations and field renames.

## Details

Vertex AI is introducing 'Semantic Governance' with two new resources: SemanticGovernancePolicyEngine (a singleton per location) and SemanticGovernancePolicies. The Agent Platform is also seeing a major refactor: the `interactions` resource has been moved from the root to a location-nested path. Developers using Agent Tools should note that the `mcp` type has been renamed to `mcp_server`. Additionally, `skillId` is now a required parameter for skill creation, and several response formats have transitioned from `URL` to `URI` enum values. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `AI` `Vertex AI` `Governance` `Agents` `Breaking Change`
