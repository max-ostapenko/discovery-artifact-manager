---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Governance Engines and Agent Anomaly Detection"
impact: high
breaking: true
tags: ["agents", "governance", "breaking-change"]
interesting_score: 8
---

# Vertex AI Beta: Governance Engines and Agent Anomaly Detection

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces new governance and anomaly detection resources for Agents while cleaning up GenAI schema naming. Note several breaking changes to parameter naming and resource requirements.

## Details

Vertex AI has added the `SemanticGovernancePolicyEngine` resource, supporting GET and PATCH (upsert) operations, alongside a new `AgentAnomalyDetectionScope` resource. Several breaking changes were introduced: the `interactions.delete` method was removed, and query parameters for `getPoll` and `getStream` were renamed from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). Additionally, `skillId` is now a required field when creating a Skill. 

On the schema side, there is a massive renaming of GenAI-related structures (e.g., `GenaiStruct` is now `GenaiVertexV1beta1Struct`). Agent listing behavior has also been tweaked: the default `pageSize` is now 10 (down from 100), and the `orderBy` parameter now expects `created`/`updated` instead of `create_time`/`update_time`.

**Tags:** `agents` `governance` `breaking-change`
