---
date: 2026-06-10
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Beta: Semantic Governance and Agent Platform Pivot"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Agents"]
interesting_score: 8
---

# Vertex AI Beta: Semantic Governance and Agent Platform Pivot

**Date:** 2026-06-10  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine for enterprise control and undergoes a significant terminology shift toward 'Agent Platform' with several breaking changes.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI policies, alongside a new SemanticGovernancePolicy resource. Developers should note several breaking changes: the 'mcp' tool type is now 'mcp_server', the 'URL' enum value in Genai response formats has been renamed to 'URI', and 'skillId' is now a required parameter for skill creation. Additionally, the interactions.delete method has been moved under the projects.locations hierarchy, and PersistentDiskSpec now supports various Hyperdisk types including hyperdisk-ml and hyperdisk-throughput.

**Tags:** `AI` `Vertex AI` `Governance` `Agents`
