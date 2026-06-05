---
date: 2026-06-05
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill creation"
impact: high
breaking: true
tags: ["AI", "Governance", "Breaking Change", "Generative AI"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill creation

**Date:** 2026-06-05  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A significant update to the v1beta1 surface introduces a Semantic Governance framework while delivering several breaking changes to Agents, Skills, and Generative AI response formats.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies resources, enabling structured governance over AI semantics. However, developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required (previously optional), and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, the delivery enum for `AudioResponseFormat` and `ImageResponseFormat` has changed from `URL` to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports a wide range of Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `AI` `Governance` `Breaking Change` `Generative AI`
