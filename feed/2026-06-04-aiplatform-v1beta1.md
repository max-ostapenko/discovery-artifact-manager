---
date: 2026-06-04
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Hyperdisk support in Vertex AI"
impact: high
breaking: true
tags: ["governance", "infrastructure", "agents", "breaking-change"]
interesting_score: 8
---

# Semantic Governance and Hyperdisk support in Vertex AI

**Date:** 2026-06-04  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a Semantic Governance Policy Engine and expands infrastructure options with Hyperdisk support, alongside several breaking changes to Skills and Agents APIs.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, enabling structured policy management within locations. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`), which is critical for high-performance AI workloads. Several breaking changes are included: the `skillId` parameter in `skills.create` is now Required rather than Optional, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `AudioResponseFormat` and `ImageResponseFormat` have transitioned from `URL` to `URI` in their delivery enums.

**Tags:** `governance` `infrastructure` `agents` `breaking-change`
