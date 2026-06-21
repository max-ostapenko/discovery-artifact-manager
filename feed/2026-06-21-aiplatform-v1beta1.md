---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: New Governance Tools and Breaking Agent Changes"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Agents", "Governance"]
interesting_score: 8
---

# Vertex AI Beta: New Governance Tools and Breaking Agent Changes

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance and Anomaly Detection for Agents, while implementing several breaking changes to the Interactions and Skills APIs, including parameter renames and required fields.

## Details

Vertex AI has added the SemanticGovernancePolicyEngine singleton and AgentAnomalyDetectionScope resources to enhance agent management and monitoring. However, developers should be aware of several breaking changes: the interactions.delete method has been removed, and parameters in interactions.getPoll and interactions.getStream have been renamed from snake_case to camelCase (e.g., last_event_id is now lastEventId). Additionally, the skillId parameter in the skills.create method has transitioned from optional to required.

Other notable changes include the renaming of delivery enum values from URL to URI in AudioResponseFormat and ImageResponseFormat schemas. Many internal schema references have also been updated to include the GenaiVertexV1beta1 prefix, which may affect direct API consumers using static types.

**Tags:** `AI` `Vertex AI` `Agents` `Governance`
