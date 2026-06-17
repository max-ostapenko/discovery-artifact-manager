---
date: 2026-06-17
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI v1beta1: Agent Platform Refactor & Breaking Changes"
impact: high
breaking: true
tags: ["breaking-change", "agents", "genai", "governance"]
interesting_score: 9
---

# Vertex AI v1beta1: Agent Platform Refactor & Breaking Changes

**Date:** 2026-06-17  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the AI Platform beta introduces Semantic Governance and Agent Anomaly Detection while implementing breaking changes to Skills and Interaction parameters.

## Details

This update includes significant breaking changes: `skillId` is now a required parameter for `skills.create`, and several interaction parameters have transitioned from snake_case to camelCase (e.g., `last_event_id` to `lastEventId`). A new `SemanticGovernancePolicyEngine` singleton resource has been added for policy management, alongside `AgentAnomalyDetectionScopes`. Developers using GenAI features will notice a major schema refactor where `GenaiVertexV1beta1ContentList` replaces several specialized sub-content lists. Additionally, the API is shifting terminology from 'Vertex AI' to 'Agent Platform' in several resource descriptions and has added support for Hyperdisk types in `PersistentDiskSpec`.

**Tags:** `breaking-change` `agents` `genai` `governance`
