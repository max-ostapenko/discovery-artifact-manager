---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Renames and New Governance Tools"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "vertex-ai"]
interesting_score: 9
---

# Vertex AI Beta: Breaking Renames and New Governance Tools

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 undergoes a significant cleanup, introducing breaking parameter renames, removing interaction deletion, and adding new governance and anomaly detection resources.

## Details

This update includes several breaking changes: the `interactions.delete` method has been removed, and query parameters for `getPoll` and `getStream` have been renamed from snake_case to camelCase (e.g., `include_input` is now `includeInput`). Additionally, `skillId` is now a required field for Skill creation. On the feature side, the API introduces `SemanticGovernancePolicyEngine`, a singleton resource for managing policy states, and `AgentAnomalyDetectionScope` for monitoring agent behavior. Developers should also note that Agent list operations now use `created` and `updated` for ordering instead of `create_time` and `update_time`.

**Tags:** `breaking-change` `agents` `governance` `vertex-ai`
