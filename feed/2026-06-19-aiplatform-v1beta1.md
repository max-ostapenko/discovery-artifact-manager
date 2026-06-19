---
date: 2026-06-19
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes and Governance Tools"
impact: high
breaking: true
tags: ["breaking-change", "genai", "governance", "agents"]
interesting_score: 9
---

# Vertex AI Beta: Breaking Changes and Governance Tools

**Date:** 2026-06-19  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the v1beta1 surface introduces breaking changes to the Interactions API, renames several parameters to standard camelCase, and adds new resources for Semantic Governance and Agent Anomaly Detection.

## Details

This update contains several breaking changes: the `interactions.delete` method has been removed, and query parameters `include_input` and `last_event_id` in the `getPoll` and `getStream` methods have been renamed to `includeInput` and `lastEventId`. Additionally, `skillId` is now a required parameter in `skills.create`. New management resources include `SemanticGovernancePolicyEngine` for policy management and `AgentAnomalyDetectionScope` for monitoring. Developers should also note a significant schema refactor where many GenAI-related types were renamed (e.g., `GenaiStruct` to `GenaiVertexV1beta1Struct`) and the `URL` enum value for audio/image delivery was changed to `URI`.

**Tags:** `breaking-change` `genai` `governance` `agents`
