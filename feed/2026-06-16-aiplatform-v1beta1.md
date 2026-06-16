---
date: 2026-06-16
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Agent API Changes"
impact: high
breaking: true
tags: ["agents", "genai", "breaking-change", "governance"]
interesting_score: 8
---

# Semantic Governance and Breaking Agent API Changes

**Date:** 2026-06-16  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces Semantic Governance and Anomaly Detection for agents, while enforcing stricter requirements for Skill creation and renaming several core fields and types.

## Details

The v1beta1 surface sees significant movement in the Agent and GenAI space. New resources include `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope`. However, several breaking changes are present: the `interactions.delete` method has been removed, and `skillId` is now a required parameter for `skills.create`. Additionally, several fields have been renamed for consistency: `include_input` and `last_event_id` are now camelCased as `includeInput` and `lastEventId`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Response formats for audio and images have also transitioned from using `URL` to `URI` terminology. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types including `hyperdisk-ml` and `hyperdisk-balanced`.

**Tags:** `agents` `genai` `breaking-change` `governance`
