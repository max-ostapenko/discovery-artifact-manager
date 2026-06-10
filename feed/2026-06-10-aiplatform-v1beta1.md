---
date: 2026-06-10
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Agent Platform updates"
impact: high
breaking: true
tags: ["AI", "Governance", "Breaking Change", "Agents"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and Agent Platform updates

**Date:** 2026-06-10  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine and several breaking changes to the Agent and Skill APIs, including required IDs and renamed enum values.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI governance policies at the location level, along with a dedicated SemanticGovernancePolicies resource. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, the delivery format for audio and image responses has transitioned from `URL` to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`. There is also a visible branding shift in documentation from 'Vertex AI' to 'Agent Platform' for specific resource descriptions.

**Tags:** `AI` `Governance` `Breaking Change` `Agents`
