---
date: 2026-06-10
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Agent API Changes"
impact: high
breaking: true
tags: ["breaking-change", "generative-ai", "governance", "agents"]
interesting_score: 8
---

# Semantic Governance and Breaking Agent API Changes

**Date:** 2026-06-10  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 introduces a new Semantic Governance Policy Engine while rolling out several breaking changes to Agent tools, Skill creation, and response formats.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, enabling location-level AI governance. However, developers should note several breaking changes: the `mcp` tool type in `AgentTool` has been renamed to `mcp_server`, and the `URL` enum value in `AudioResponseFormat` and `ImageResponseFormat` is now `URI`. Additionally, `skillId` is now a required parameter for `skills.create`, and the `interactions.delete` method has been moved under the `projects.locations` hierarchy.

On the infrastructure side, `PersistentDiskSpec` now supports Hyperdisk types, including `hyperdisk-balanced`, `hyperdisk-ml`, and `hyperdisk-throughput`. There is also a visible terminology shift in documentation from 'Vertex AI' to 'Agent Platform' across several resource descriptions.

**Tags:** `breaking-change` `generative-ai` `governance` `agents`
