---
date: 2026-06-13
api: aiplatform.v1beta1
service: Vertex AI
title: "Agent Platform Refactor and Semantic Governance Tools"
impact: high
breaking: true
tags: ["breaking-change", "agents", "governance", "genai"]
interesting_score: 9
---

# Agent Platform Refactor and Semantic Governance Tools

**Date:** 2026-06-13  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A massive update to the v1beta1 surface introduces Semantic Governance, Agent Anomaly Detection, and Hyperdisk support, alongside several breaking changes to interactions and skills.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI policy states, and AgentAnomalyDetectionScopes for monitoring agent behavior. Significant breaking changes include the removal of the interactions.delete method and the renaming of parameters in interactions.getPoll and interactions.getStream (e.g., last_event_id is now lastEventId). Additionally, skillId is now a required parameter when creating Skills, and several schema references for GenAI function results have been consolidated into a generic ContentList. Developers should also note the deprecation of Google Maps contextual widgets and the addition of multiple Hyperdisk types (ML, Balanced, Throughput) to the PersistentDiskSpec.

**Tags:** `breaking-change` `agents` `governance` `genai`
