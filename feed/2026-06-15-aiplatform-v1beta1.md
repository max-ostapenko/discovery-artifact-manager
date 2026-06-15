---
date: 2026-06-15
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI v1beta1: Agent Platform Rebrand & Breaking Changes"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "infrastructure"]
interesting_score: 9
---

# Vertex AI v1beta1: Agent Platform Rebrand & Breaking Changes

**Date:** 2026-06-15  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the Vertex AI beta API introduces 'Agent Platform' branding, renames interaction parameters, and adds new governance and anomaly detection resources.

## Details

This update includes several breaking changes: the `interactions.delete` method has been removed, and parameters for `interactions.getPoll` and `interactions.getStream` have been renamed from snake_case (`include_input`, `last_event_id`) to camelCase (`includeInput`, `lastEventId`). New singleton resources for `SemanticGovernancePolicyEngine` and `AgentAnomalyDetectionScope` are now available. Additionally, `PersistentDiskSpec` has been expanded to support Hyperdisk types including `hyperdisk-ml` and `hyperdisk-throughput`. Developers should also note a terminology shift in documentation from 'Vertex AI' to 'Agent Platform' for specific resource descriptions.

**Tags:** `breaking-change` `agents` `governance` `infrastructure`
