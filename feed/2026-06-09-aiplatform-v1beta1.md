---
date: 2026-06-09
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Agent API Changes"
impact: high
breaking: true
tags: ["Vertex AI", "Generative AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance and Breaking Agent API Changes

**Date:** 2026-06-09  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance framework for AI policy management alongside several breaking changes to Agent and GenAI response schemas.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies resources, allowing developers to programmatically manage AI guardrails. However, there are several breaking changes to be aware of: the GenAI response formats for audio and images have renamed the 'URL' enum value to 'URI', and the AgentTool type 'mcp' has been renamed to 'mcp_server'. Additionally, the 'skillId' parameter is now required when creating Skills, and the 'interactions.delete' method has been moved to a location-nested path. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types including hyperdisk-ml and hyperdisk-throughput.

**Tags:** `Vertex AI` `Generative AI` `Governance` `Agents` `Breaking Change`
