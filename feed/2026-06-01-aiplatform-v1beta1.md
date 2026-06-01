---
date: 2026-06-01
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Hyperdisk support"
impact: high
breaking: true
tags: ["AI", "Governance", "Storage", "Agents"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and Hyperdisk support

**Date:** 2026-06-01  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a Semantic Governance Policy Engine and expands storage options with Hyperdisk support, alongside several breaking changes to Skills and Agents.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI governance policies, including new methods for upserting and retrieving policies. Developers using the Skills API should note that `skillId` is now a required parameter in `skills.create`. Additionally, the Agent API has been refined: the `mcp` tool type is now `mcp_server`, and the default `pageSize` for listing agents has been reduced from 100 to 10. Infrastructure-wise, `PersistentDiskSpec` now supports high-performance Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `AI` `Governance` `Storage` `Agents`
