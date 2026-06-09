---
date: 2026-06-09
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI Governance Engine and Agent Platform Refactor"
impact: high
breaking: true
tags: ["Vertex AI", "AI Governance", "Generative AI", "Breaking Change"]
interesting_score: 9
---

# Vertex AI Governance Engine and Agent Platform Refactor

**Date:** 2026-06-09  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 introduces a new Semantic Governance Policy Engine and shifts several resources toward the 'Agent Platform' branding. This update includes multiple breaking changes to enums and required parameters.

## Details

A new Semantic Governance Policy Engine has been introduced as a singleton resource per location, allowing developers to manage SemanticGovernancePolicies via new GET, PATCH (upsert), and CREATE methods. Significant breaking changes include the renaming of the 'URL' enum value to 'URI' in Audio and Image response formats, and the renaming of the 'mcp' tool type to 'mcp_server' in AgentTool. Additionally, the `skillId` parameter in the `skills.create` method has been changed from optional to required. On the infrastructure side, PersistentDiskSpec now supports a wide array of Hyperdisk types, including hyperdisk-ml and hyperdisk-throughput.

**Tags:** `Vertex AI` `AI Governance` `Generative AI` `Breaking Change`
