---
date: 2026-06-14
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Agent Platform Rebrand & Governance Tools"
impact: high
breaking: true
tags: ["AI", "Agents", "Governance", "Breaking Change"]
interesting_score: 8
---

# Vertex AI Beta: Agent Platform Rebrand & Governance Tools

**Date:** 2026-06-14  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 surface introduces the Semantic Governance Policy Engine and Agent Anomaly Detection, alongside a significant documentation shift toward 'Agent Platform.'

## Details

This update introduces several new resource types, including the SemanticGovernancePolicyEngine (a singleton for policy management) and AgentAnomalyDetectionScope. Developers should note a shift in naming conventions: interaction parameters like `include_input` and `last_event_id` have been replaced by camelCase versions (`includeInput`, `lastEventId`). Additionally, the AgentTool type `mcp` has been renamed to `mcp_server`. On the infrastructure side, PersistentDiskSpec now supports a wide array of Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput. There is also a notable deprecation of Google Maps contextual widgets within grounding metadata.

**Tags:** `AI` `Agents` `Governance` `Breaking Change`
