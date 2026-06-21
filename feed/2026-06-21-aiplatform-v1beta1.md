---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes and Governance Updates"
impact: high
breaking: true
tags: ["breaking-change", "generative-ai", "governance", "agents"]
interesting_score: 8
---

# Vertex AI Beta: Breaking Changes and Governance Updates

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI's v1beta1 surface has undergone a significant cleanup, introducing breaking changes to parameter naming, tool types, and resource requirements alongside new governance features.

## Details

This update includes several breaking changes: the `interactions.delete` method has been removed, and the `skillId` parameter in `skills.create` is now required. Parameter naming in `interactions.getPoll` and `getStream` has shifted from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). Additionally, the `AgentTool` type `mcp` was renamed to `mcp_server`, and `Audio/ImageResponseFormat` enums changed `URL` to `URI`. On the feature side, a new `SemanticGovernancePolicyEngine` singleton and `AgentAnomalyDetectionScope` resources have been introduced to enhance policy management and monitoring.

**Tags:** `breaking-change` `generative-ai` `governance` `agents`
