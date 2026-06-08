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

This update introduces a new Semantic Governance Policy Engine and several breaking changes to the Agent and Skill APIs, including required identifiers and renamed enum values.

## Details

A new singleton resource, `SemanticGovernancePolicyEngine`, has been added along with `SemanticGovernancePolicy` management methods (`create`, `get`, `update`, `delete`). Developers using the Agent Platform should note several breaking changes: `skillId` is now a required parameter in `skills.create`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, the delivery format for audio and image responses has changed the enum value `URL` to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
