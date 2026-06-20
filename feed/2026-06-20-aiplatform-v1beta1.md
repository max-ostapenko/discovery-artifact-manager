---
date: 2026-06-20
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Semantic Governance and Agent Monitoring"
impact: high
breaking: true
tags: ["AI Agents", "Governance", "Breaking Change"]
interesting_score: 8
---

# Vertex AI Beta: Semantic Governance and Agent Monitoring

**Date:** 2026-06-20  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces new governance and anomaly detection resources for AI Agents while enforcing stricter requirements for Skills and standardizing parameter naming.

## Details

Vertex AI has added a new singleton resource, `SemanticGovernancePolicyEngine`, with GET and PATCH (upsert) methods for managing policy states. A new `AgentAnomalyDetectionScope` resource is also available for monitoring agent behavior. Several breaking changes were introduced: the `interactions.delete` method was removed, `skillId` is now a required parameter when creating Skills, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, query parameters for interaction polling and streaming have been standardized from snake_case to camelCase (e.g., `includeInput`, `lastEventId`), and `Interaction.steps` is now a required field in the schema.

**Tags:** `AI Agents` `Governance` `Breaking Change`
