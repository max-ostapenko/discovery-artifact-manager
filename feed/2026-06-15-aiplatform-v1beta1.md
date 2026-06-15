---
date: 2026-06-15
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent Governance and Breaking Skill Changes"
impact: high
breaking: true
tags: ["agents", "genai", "governance", "breaking-change"]
interesting_score: 8
---

# Vertex AI Beta: Agent Governance and Breaking Skill Changes

**Date:** 2026-06-15  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance and Anomaly Detection for agents while enforcing stricter requirements for Skill creation and renaming several GenAI response parameters.

## Details

Vertex AI is shifting terminology toward 'Agent Platform' and introducing new governance tools. A new singleton resource, `SemanticGovernancePolicyEngine`, has been added for policy management, alongside `AgentAnomalyDetectionScope` for monitoring. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now Required (previously Optional), and the `interactions.delete` method has been removed. Additionally, GenAI response formats for audio and images have transitioned from `URL` to `URI` enums, and interaction query parameters have been renamed from snake_case to camelCase (e.g., `last_event_id` to `lastEventId`). Support for various Hyperdisk types has also been added to `PersistentDiskSpec`.

**Tags:** `agents` `genai` `governance` `breaking-change`
