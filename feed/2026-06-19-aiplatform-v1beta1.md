---
date: 2026-06-19
api: aiplatform.v1beta1
service: Vertex AI
title: "Breaking Changes to Vertex AI Agents and Interactions"
impact: high
breaking: true
tags: ["agents", "genai", "breaking-change"]
interesting_score: 8
---

# Breaking Changes to Vertex AI Agents and Interactions

**Date:** 2026-06-19  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces several breaking changes to the Vertex AI Agent and Interaction APIs, including parameter renames, required field updates, and resource restructuring, alongside new governance features.

## Details

The API sees significant churn in the Agentic AI space. Breaking changes include the removal of the `interactions.delete` method and the renaming of query parameters in `getPoll` and `getStream` from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). Creating a `Skill` now requires a `skillId`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `agents.list` sorting fields have changed from `create_time`/`update_time` to `created`/`updated`. On the feature side, new resources for `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope` have been added to improve policy management and monitoring.

**Tags:** `agents` `genai` `breaking-change`
