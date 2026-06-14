---
date: 2026-06-14
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent Platform Refactor"
impact: high
breaking: true
tags: ["agents", "governance", "breaking-change", "generative-ai"]
interesting_score: 9
---

# Semantic Governance and Agent Platform Refactor

**Date:** 2026-06-14  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 surface introduces Semantic Governance, Agent Anomaly Detection, and a shift toward 'Agent Platform' branding with significant breaking changes to parameter naming.

## Details

This update introduces the `SemanticGovernancePolicyEngine` as a singleton resource and adds `AgentAnomalyDetectionScope` for enhanced monitoring. Developers should note several breaking changes: the `interactions.delete` method has been removed, and multiple parameters have transitioned from snake_case to camelCase (e.g., `include_input` is now `includeInput`). Additionally, the `AgentTool` type `mcp` has been renamed to `mcp_server`, and Google Maps contextual widgets in grounding are now deprecated. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`.

**Tags:** `agents` `governance` `breaking-change` `generative-ai`
