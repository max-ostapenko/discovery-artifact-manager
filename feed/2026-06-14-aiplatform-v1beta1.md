---
date: 2026-06-14
api: aiplatform.v1beta1
service: Vertex AI
title: "Agent Platform Refactor and Semantic Governance Tools"
impact: high
breaking: true
tags: ["AI", "Agents", "Governance", "Breaking Change"]
interesting_score: 9
---

# Agent Platform Refactor and Semantic Governance Tools

**Date:** 2026-06-14  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 surface introduces Semantic Governance, Agent anomaly detection, and a shift in terminology toward 'Agent Platform.' Note several breaking changes including parameter renames and the removal of interaction deletion.

## Details

This update introduces the SemanticGovernancePolicyEngine singleton and AgentAnomalyDetectionScopes for better control over AI agents. Significant refactoring is evident: the 'interactions.delete' method has been removed, and query parameters for interaction polling/streaming have transitioned from snake_case (include_input) to camelCase (includeInput). Additionally, the 'AgentTool' type 'mcp' has been renamed to 'mcp_server', and 'skillId' is now a required field when creating skills. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types including hyperdisk-ml and hyperdisk-balanced.

**Tags:** `AI` `Agents` `Governance` `Breaking Change`
