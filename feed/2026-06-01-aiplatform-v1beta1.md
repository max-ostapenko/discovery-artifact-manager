---
date: 2026-06-01
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Hyperdisk support in Vertex AI"
impact: high
breaking: true
tags: ["AI Governance", "Vertex AI", "Storage", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance and Hyperdisk support in Vertex AI

**Date:** 2026-06-01  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and expands storage options with Hyperdisk support, alongside several breaking changes to the Agents and Skills APIs.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI governance policies, including new methods for retrieval and upserting policies. The PersistentDiskSpec schema now supports multiple Hyperdisk types, including hyperdisk-balanced, hyperdisk-extreme, and hyperdisk-ml. Several breaking changes were introduced: the 'skillId' parameter in the skills.create method is now Required instead of Optional, and the 'URL' enum value in GenaiVertexV1beta1 response formats has been renamed to 'URI'. Additionally, AgentTool types have been refined, specifically changing 'mcp' to 'mcp_server'.

**Tags:** `AI Governance` `Vertex AI` `Storage` `Breaking Change`
