---
date: 2026-06-13
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent Platform Rebrand & Governance Tools"
impact: high
breaking: true
tags: ["AI Agents", "Breaking Change", "Governance", "GenAI"]
interesting_score: 9
---

# Vertex AI Beta: Agent Platform Rebrand & Governance Tools

**Date:** 2026-06-13  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 is shifting toward a dedicated 'Agent Platform' architecture, introducing new governance and anomaly detection resources while implementing breaking changes to interaction parameters.

## Details

This update introduces several major components: the `SemanticGovernancePolicyEngine` for policy management and `AgentAnomalyDetectionScope` for monitoring. Developers building agents should note the addition of `mcp_server` to `AgentTool`, enabling Model Context Protocol integration. On the infrastructure side, `PersistentDiskSpec` now supports multiple Hyperdisk types (ML, Balanced, Throughput). 

Breaking changes are present in the `interactions` resource: the `delete` method has been removed, and query parameters `include_input` and `last_event_id` have been renamed to camelCase (`includeInput`, `lastEventId`) in the `getPoll` and `getStream` methods. Additionally, Google Maps contextual widgets in grounding are now deprecated and slated for removal.

**Tags:** `AI Agents` `Breaking Change` `Governance` `GenAI`
