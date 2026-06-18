---
date: 2026-06-18
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent API Refactor and Governance Tools"
impact: high
breaking: true
tags: ["agents", "generative-ai", "breaking-change", "governance"]
interesting_score: 9
---

# Vertex AI Beta: Agent API Refactor and Governance Tools

**Date:** 2026-06-18  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the v1beta1 surface, introducing Semantic Governance and Anomaly Detection while breaking several existing Agent and Interaction parameters to align with naming standards.

## Details

This update introduces significant breaking changes and new resources. Key breaking changes include renaming snake_case parameters to camelCase in `interactions.getPoll` and `getStream` (e.g., `include_input` is now `includeInput`), and the removal of the `interactions.delete` method. The `skillId` parameter in Skill creation has moved from optional to required. Additionally, several schemas have been namespaced, such as `GenaiStruct` becoming `GenaiVertexV1beta1Struct`, and the `URL` enum value in response formats has been changed to `URI`.

On the feature side, developers can now manage `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope` resources. The Agent API also received a cleanup, standardizing ID patterns and renaming the `mcp` tool type to `mcp_server`. New stream resumption capabilities are available via the `lastEventId` parameter in interaction methods.

**Tags:** `agents` `generative-ai` `breaking-change` `governance`
