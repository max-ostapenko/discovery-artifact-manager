---
date: 2026-06-20
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Breaking Changes to Agents and Governance"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI Beta: Breaking Changes to Agents and Governance

**Date:** 2026-06-20  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces significant breaking changes to the Agent and Interaction APIs, including renamed parameters, new required fields, and the removal of the interaction delete method.

## Details

The Vertex AI beta surface is undergoing a major cleanup. Breaking changes include the removal of the `interactions.delete` method and the renaming of query parameters in `getPoll` and `getStream` from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). Additionally, `skillId` is now a required parameter for `skills.create`, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. On the feature side, two new resource types have been introduced: `SemanticGovernancePolicyEngine` for managing singleton governance policies and `AgentAnomalyDetectionScope` for monitoring agent behavior. Developers should also note that `AudioResponseFormat` and `ImageResponseFormat` enums have shifted from `URL` to `URI` naming.

**Tags:** `AI` `Vertex AI` `Agents` `Breaking Change`
