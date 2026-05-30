---
date: 2026-05-30
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent API Refinement"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Storage"]
interesting_score: 8
---

# Semantic Governance and Agent API Refinement

**Date:** 2026-05-30  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and applies several breaking changes to the Agents and Skills APIs.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, enabling location-level AI governance. The Agents API sees significant churn: the `AgentTool` type `mcp` has been renamed to `mcp_server`, and several response formats have transitioned from `URL` to `URI` naming conventions. Additionally, `skillId` is now a required parameter for Skill creation, and the `PersistentDiskSpec` schema has been expanded to support high-performance Hyperdisk types (Balanced, Extreme, ML, and Throughput).

**Tags:** `AI` `Governance` `Agents` `Storage`
