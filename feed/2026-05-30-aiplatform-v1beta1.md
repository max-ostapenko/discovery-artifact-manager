---
date: 2026-05-30
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Changes to Skills and Tools"
impact: high
breaking: true
tags: ["governance", "genai", "agents", "infrastructure"]
interesting_score: 8
---

# Semantic Governance and Breaking Changes to Skills and Tools

**Date:** 2026-05-30  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while implementing several breaking changes to Skills, Agent Tools, and GenAI response formats.

## Details

This update introduces the `SemanticGovernancePolicyEngine` (a singleton resource) and `SemanticGovernancePolicies` for managing AI governance. Several breaking changes are included: the `skillId` parameter in `skills.create` is now required, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and GenAI response formats for Audio and Image have transitioned the `URL` enum value to `URI`. Additionally, `PersistentDiskSpec` now supports multiple Hyperdisk types including `hyperdisk-balanced`, `hyperdisk-extreme`, and `hyperdisk-ml`.

**Tags:** `governance` `genai` `agents` `infrastructure`
