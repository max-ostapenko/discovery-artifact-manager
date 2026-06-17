---
date: 2026-06-17
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent Platform Shift & Breaking Changes"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "genai"]
interesting_score: 8
---

# Vertex AI Beta: Agent Platform Shift & Breaking Changes

**Date:** 2026-06-17  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the v1beta1 surface introduces Semantic Governance and Anomaly Detection while renaming several parameters and deprecating Google Maps widgets.

## Details

This update includes significant breaking changes and new resource types. The `interactions.delete` method has been removed, and query parameters for `getPoll` and `getStream` have shifted from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). Additionally, `skillId` is now a required parameter in the `skills.create` method. 

New capabilities include the `SemanticGovernancePolicyEngine` singleton for managing governance states and `AgentAnomalyDetectionScope` for monitoring. Infrastructure-wise, `PersistentDiskSpec` now supports various Hyperdisk types (ML, Throughput, etc.). Developers using Grounding with Google Maps should note that contextual widgets are now deprecated and slated for removal. There is also a visible branding shift in documentation from 'Vertex AI' to 'Agent Platform' across several resource descriptions.

**Tags:** `breaking-change` `agents` `governance` `genai`
