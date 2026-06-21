---
date: 2026-06-21
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent Anomaly Detection"
impact: high
breaking: true
tags: ["generative-ai", "agents", "governance", "breaking-change"]
interesting_score: 9
---

# Semantic Governance and Agent Anomaly Detection

**Date:** 2026-06-21  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update to the v1beta1 surface introduces governance policy engines and anomaly detection for agents, while enforcing stricter requirements on Skill creation and updating Agent list defaults.

## Details

This update introduces the `SemanticGovernancePolicyEngine`, a singleton resource for managing AI policies via a new upsert-capable `PATCH` method. It also adds `AgentAnomalyDetectionScopes` for monitoring agent behavior. Several breaking changes are included: `skillId` is now a required parameter in `skills.create`, and the `orderBy` fields for listing agents have changed from `create_time`/`update_time` to `created`/`updated`. Additionally, the default `pageSize` for listing agents has been significantly reduced from 100 to 10.

**Tags:** `generative-ai` `agents` `governance` `breaking-change`
