---
date: 2026-06-16
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI v1beta1: Breaking Changes and Agent Platform Pivot"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "storage"]
interesting_score: 8
---

# Vertex AI v1beta1: Breaking Changes and Agent Platform Pivot

**Date:** 2026-06-16  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the AI Platform beta surface introduces new governance and anomaly detection resources while enforcing several breaking changes to Interactions, Skills, and Tool definitions.

## Details

This update includes several breaking changes: the `interactions.delete` method has been removed, and query parameters for `getPoll` and `getStream` have been renamed from snake_case to camelCase (e.g., `last_event_id` is now `lastEventId`). Additionally, `skillId` is now a required parameter for Skill creation, and the `mcp` tool type has been renamed to `mcp_server`. 

On the feature side, a new singleton resource `SemanticGovernancePolicyEngine` is available for managing policy states, and `AgentAnomalyDetectionScopes` has been added. Developers can now also specify various Hyperdisk types (ML, Extreme, Balanced) in `PersistentDiskSpec`. Notably, much of the documentation has been updated to refer to the 'Agent Platform' rather than 'Vertex AI', signaling a shift in the service's positioning.

**Tags:** `breaking-change` `agents` `governance` `storage`
