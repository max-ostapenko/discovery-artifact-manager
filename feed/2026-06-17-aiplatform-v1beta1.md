---
date: 2026-06-17
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent Platform Refactor & Breaking Changes"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "storage"]
interesting_score: 9
---

# Vertex AI Beta: Agent Platform Refactor & Breaking Changes

**Date:** 2026-06-17  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 surface introduces Semantic Governance, Agent Anomaly Detection, and Hyperdisk support, alongside several breaking changes to existing resources.

## Details

This update signals a significant shift toward the 'Agent Platform' branding and architecture. Key additions include the `SemanticGovernancePolicyEngine` (a singleton resource for policy management) and `AgentAnomalyDetectionScopes`. Developers using the `interactions` resource should note that the `delete` method has been removed, and parameters for `getPoll` and `getStream` have migrated from snake_case (`include_input`) to camelCase (`includeInput`). Furthermore, `skillId` is now a required parameter when creating a Skill, and `PersistentDiskSpec` now supports various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`).

**Tags:** `breaking-change` `agents` `governance` `storage`
