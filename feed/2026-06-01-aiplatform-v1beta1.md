---
date: 2026-06-01
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Agent/Skill Changes"
impact: high
breaking: true
tags: ["ai", "governance", "agents", "breaking-change"]
interesting_score: 8
---

# Semantic Governance and Breaking Agent/Skill Changes

**Date:** 2026-06-01  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while implementing several breaking changes to Agents, Skills, and media response formats.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicy resources, allowing for location-based AI governance. Significant breaking changes include renaming the AgentTool type 'mcp' to 'mcp_server' and making 'skillId' a required parameter in the Skills create method. Additionally, the delivery enum for Audio and Image response formats has changed from 'URL' to 'URI'. On the infrastructure side, PersistentDiskSpec now supports a wide range of Hyperdisk types including hyperdisk-balanced, hyperdisk-extreme, and hyperdisk-ml.

**Tags:** `ai` `governance` `agents` `breaking-change`
