---
date: 2026-06-03
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Governance Engine and Breaking GenAI Enum Changes"
impact: high
breaking: true
tags: ["Vertex AI", "Governance", "GenAI", "Breaking Change"]
interesting_score: 8
---

# Vertex AI Governance Engine and Breaking GenAI Enum Changes

**Date:** 2026-06-03  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while implementing several breaking changes to GenAI response formats, Agent tool types, and Skill creation parameters.

## Details

This update introduces the Semantic Governance Policy Engine and associated SemanticGovernancePolicy resources for location-based AI policy management. Significant breaking changes include renaming the 'URL' enum value to 'URI' in both AudioResponseFormat and ImageResponseFormat schemas, and renaming the 'mcp' tool type to 'mcp_server' in AgentTool. Additionally, the `skillId` parameter in the skills.create method has been changed from optional to required. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput.

**Tags:** `Vertex AI` `Governance` `GenAI` `Breaking Change`
