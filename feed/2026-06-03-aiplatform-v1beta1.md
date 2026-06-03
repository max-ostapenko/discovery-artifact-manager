---
date: 2026-06-03
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and refines Agents API"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and refines Agents API

**Date:** 2026-06-03  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and makes several breaking changes to the Agents and Skills APIs, including required IDs and renamed enum values.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies resources for managing AI-related policies. Significant breaking changes include making `skillId` a required parameter in the Skills creation method and renaming the `mcp` tool type to `mcp_server` within the AgentTool schema. Additionally, PersistentDiskSpec has been expanded to support various Hyperdisk types (e.g., hyperdisk-ml, hyperdisk-balanced), and GenAI response formats have transitioned from using 'URL' to 'URI' terminology.

**Tags:** `AI` `Vertex AI` `Governance` `Agents` `Breaking Change`
