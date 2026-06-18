---
date: 2026-06-18
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent Refactoring and Governance Policies"
impact: high
breaking: true
tags: ["agents", "genai", "governance", "breaking-change"]
interesting_score: 8
---

# Vertex AI Beta: Agent Refactoring and Governance Policies

**Date:** 2026-06-18  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the v1beta1 surface introduces Semantic Governance Policies and Agent Anomaly Detection while significantly refactoring GenAI and Agent schema structures.

## Details

This update includes several breaking changes: the `interactions.delete` method has been removed, and multiple parameters in `getPoll` and `getStream` have been renamed from snake_case to camelCase (e.g., `include_input` to `includeInput`). The `AgentTool` type `mcp` has been renamed to `mcp_server`, and the `URL` enum in response formats is now `URI`. On the feature side, new resources for `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope` are now available at the location level. Additionally, many internal GenAI schemas have been namespaced (e.g., `GenaiStruct` is now `GenaiVertexV1beta1Struct`), and `Interaction.steps` is now a required field.

**Tags:** `agents` `genai` `governance` `breaking-change`
