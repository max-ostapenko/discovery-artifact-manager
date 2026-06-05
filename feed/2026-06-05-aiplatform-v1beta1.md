---
date: 2026-06-05
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent Platform Refinements"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "generative-ai"]
interesting_score: 8
---

# Semantic Governance and Agent Platform Refinements

**Date:** 2026-06-05  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework and makes several breaking changes to response formats and resource paths within the Agent Platform.

## Details

Vertex AI has introduced a new Semantic Governance suite, including the `SemanticGovernancePolicyEngine` (a singleton resource) and `SemanticGovernancePolicies` for managing AI behavior. The Agent Platform is also seeing significant updates: `AgentTool` now explicitly supports `mcp_server` types, and `PersistentDiskSpec` has been expanded to include various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`). Note that many documentation strings have shifted terminology from 'Vertex AI' to 'Agent Platform'.

**Tags:** `governance` `agents` `breaking-change` `generative-ai`
