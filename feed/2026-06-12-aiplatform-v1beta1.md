---
date: 2026-06-12
api: aiplatform.v1beta1
service: Vertex AI (AI Platform)
title: "Semantic Governance and Agent Platform Refactor"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "genai"]
interesting_score: 8
---

# Semantic Governance and Agent Platform Refactor

**Date:** 2026-06-12  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance Policy Engine and significantly refactors the Agent Platform surface with several breaking changes to enums and required fields.

## Details

A new suite of resources for AI governance has been added, including `SemanticGovernancePolicyEngine` (a singleton per location) and `SemanticGovernancePolicies`. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, GenAI response formats for audio and images have changed their delivery enum from `URL` to `URI`. The documentation also reflects a major branding shift from 'Vertex AI' to 'Agent Platform' across many resource descriptions.

New infrastructure options include support for various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`) in `PersistentDiskSpec`. Finally, the default `pageSize` for `agents.list` has been reduced from 100 to 10, which may impact existing pagination logic if not explicitly handled.

**Tags:** `governance` `agents` `breaking-change` `genai`
