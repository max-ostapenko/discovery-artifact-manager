---
date: 2026-06-15
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI v1beta1: Semantic Governance and Agent Refactor"
impact: high
breaking: true
tags: ["AI", "Agents", "Governance", "Breaking Change"]
interesting_score: 9
---

# Vertex AI v1beta1: Semantic Governance and Agent Refactor

**Date:** 2026-06-15  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update introducing Semantic Governance Policy Engines and Agent Anomaly Detection, alongside a significant branding shift toward 'Agent Platform' and several breaking API changes.

## Details

This update introduces the `SemanticGovernancePolicyEngine` as a singleton resource and adds `AgentAnomalyDetectionScopes` for monitoring agentic workflows. Developers should note several breaking changes: the `interactions.delete` method has been removed, and `skillId` is now a required parameter when creating skills. Additionally, interaction parameters have been renamed from snake_case to camelCase (e.g., `include_input` to `includeInput`), and the `lastEventId` parameter has been added to support resuming interaction streams. Infrastructure-wise, `PersistentDiskSpec` now supports Hyperdisk types (balanced, extreme, ML, etc.).

**Tags:** `AI` `Agents` `Governance` `Breaking Change`
