---
date: 2026-06-02
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives as Skills and Agent tools break"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "infrastructure"]
interesting_score: 8
---

# Semantic Governance arrives as Skills and Agent tools break

**Date:** 2026-06-02  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while landing several breaking changes to Skills, Agent tools, and GenAI response formats.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI policies at the location level, along with a new SemanticGovernancePolicies sub-resource. However, developers should be wary of several breaking changes: the `skillId` parameter in `skills.create` is now required rather than optional, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and the `delivery` enum in GenAI response formats changed from `URL` to `URI`. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced` for high-performance workloads.

**Tags:** `governance` `agents` `breaking-change` `infrastructure`
