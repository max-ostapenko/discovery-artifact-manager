---
date: 2026-06-14
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI v1beta1: Agent Platform Shift and Breaking Changes"
impact: high
breaking: true
tags: ["agents", "governance", "breaking-change", "genai"]
interesting_score: 9
---

# Vertex AI v1beta1: Agent Platform Shift and Breaking Changes

**Date:** 2026-06-14  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the AI Platform beta introduces Semantic Governance and Anomaly Detection for agents, while introducing breaking changes to Skill creation and tool naming.

## Details

This update includes several breaking changes: the `skillId` is now required for `skills.create`, and the `mcp` tool type has been renamed to `mcp_server`. Additionally, enum values for audio and image delivery have shifted from `URL` to `URI`. New resources include `SemanticGovernancePolicyEngine` (a singleton for policy management) and `AgentAnomalyDetectionScope`. Developers using the `interactions` resource should note that `interactions.delete` has been removed, and query parameters like `include_input` and `last_event_id` have been replaced with camelCase versions (`includeInput`, `lastEventId`).

**Tags:** `agents` `governance` `breaking-change` `genai`
