---
date: 2026-06-13
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Agent Platform Evolution"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "mcp"]
interesting_score: 8
---

# Semantic Governance and Agent Platform Evolution

**Date:** 2026-06-13  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework, adds support for Model Context Protocol (MCP) servers in Agents, and includes several breaking changes to Skills and GenAI response formats.

## Details

Vertex AI is expanding its governance capabilities with the introduction of the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicy` resources, allowing for structured policy management. The Agents API now supports `mcp_server` as a tool type, enabling integration with external MCP-compliant servers. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required, and the `GenaiVertexV1beta1` schemas for Audio and Image response formats have renamed the `URL` enum value to `URI`. Additionally, the API descriptions are shifting terminology from 'Vertex AI' to 'Agent Platform' in many resource definitions.

**Tags:** `governance` `agents` `breaking-change` `mcp`
