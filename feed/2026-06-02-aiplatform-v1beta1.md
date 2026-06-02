---
date: 2026-06-02
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives alongside breaking API changes"
impact: high
breaking: true
tags: ["breaking-change", "governance", "agents", "generative-ai"]
interesting_score: 8
---

# Semantic Governance arrives alongside breaking API changes

**Date:** 2026-06-02  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while landing several breaking changes to Skills, Agents, and Generative AI response formats.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies resources, enabling structured policy management within locations. However, developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required rather than optional. In `AgentTool`, the tool type `mcp` has been renamed to `mcp_server`. Additionally, the `URL` enum value in `AudioResponseFormat` and `ImageResponseFormat` has been changed to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `breaking-change` `governance` `agents` `generative-ai`
