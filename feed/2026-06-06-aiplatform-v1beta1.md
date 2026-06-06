---
date: 2026-06-06
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Agent Platform updates"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and Agent Platform updates

**Date:** 2026-06-06  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine and associated policies, while implementing several breaking changes to Agent tools and response formats.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicy resources, enabling structured control over AI behavior. Developers should be alert to several breaking changes: the AgentTool type 'mcp' has been renamed to 'mcp_server', and the 'URL' enum value in Audio/Image response formats is now 'URI'. Additionally, skillId is now a required parameter for skill creation, and the interactions.delete method has been moved to a location-scoped path. The documentation also reflects a shift in branding from 'Vertex AI' to 'Agent Platform' for specific resource descriptions.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
