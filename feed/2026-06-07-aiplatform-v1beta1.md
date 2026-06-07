---
date: 2026-06-07
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks several enums"
impact: high
breaking: true
tags: ["governance", "breaking-change", "agents", "infrastructure"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks several enums

**Date:** 2026-06-07  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine for AI guardrails alongside several breaking changes to enums and resource requirements.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicy resources, enabling developers to manage and upsert AI governance rules at the location level. Several breaking changes are included: the GenaiVertexV1beta1 response formats for Audio and Image have renamed the 'URL' enum value to 'URI', and the AgentTool type 'mcp' has been renamed to 'mcp_server'. Additionally, 'skillId' is now a required parameter for creating skills, and the 'interactions.delete' method has been moved under the locations resource path. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types including 'hyperdisk-ml' and 'hyperdisk-balanced'.

**Tags:** `governance` `breaking-change` `agents` `infrastructure`
