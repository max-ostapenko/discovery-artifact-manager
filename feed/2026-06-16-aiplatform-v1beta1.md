---
date: 2026-06-16
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI v1beta1: Agent Platform Pivot & Governance Tools"
impact: high
breaking: true
tags: ["agents", "governance", "breaking-change", "infrastructure"]
interesting_score: 9
---

# Vertex AI v1beta1: Agent Platform Pivot & Governance Tools

**Date:** 2026-06-16  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the AI Platform beta introducing Semantic Governance, Agent Anomaly Detection, and a significant shift in branding toward 'Agent Platform'.

## Details

This update introduces the `SemanticGovernancePolicyEngine`, a singleton resource for managing AI policies, and `AgentAnomalyDetectionScope` for monitoring agent behavior. Significant breaking changes include the removal of the `interactions.delete` method and the renaming of several query parameters from snake_case to camelCase (e.g., `include_input` is now `includeInput`). The `AgentTool` schema has also been updated, renaming the `mcp` type to `mcp_server`. Additionally, `PersistentDiskSpec` now supports a wide array of Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `agents` `governance` `breaking-change` `infrastructure`
