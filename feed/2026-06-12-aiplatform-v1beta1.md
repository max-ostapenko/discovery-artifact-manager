---
date: 2026-06-12
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Hyperdisk Support in Vertex AI"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Storage"]
interesting_score: 8
---

# Semantic Governance and Hyperdisk Support in Vertex AI

**Date:** 2026-06-12  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine for AI guardrails, adds Hyperdisk support for compute resources, and makes breaking changes to GenAI response formats and Skill creation.

## Details

This update introduces the `SemanticGovernancePolicyEngine`, a singleton resource for managing AI governance at the location level, along with `SemanticGovernancePolicy` resources. The Agent Platform is seeing significant refinement, including the renaming of `mcp` tool types to `mcp_server` and a shift in documentation terminology from 'Vertex AI' to 'Agent Platform'. Infrastructure-wise, `PersistentDiskSpec` now supports high-performance Hyperdisk types (Balanced, Extreme, ML, and Throughput). Note that `interactions.delete` has been moved under the location-based resource hierarchy.

**Tags:** `AI` `Governance` `Agents` `Storage`
