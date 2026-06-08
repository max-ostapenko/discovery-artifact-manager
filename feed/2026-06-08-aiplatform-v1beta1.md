---
date: 2026-06-08
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives as Vertex AI pivots to Agent Platform"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "storage"]
interesting_score: 8
---

# Semantic Governance arrives as Vertex AI pivots to Agent Platform

**Date:** 2026-06-08  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

A major update introduces the Semantic Governance Policy Engine for AI oversight and shifts terminology toward 'Agent Platform,' while introducing several breaking changes to skills and response formats.

## Details

This update introduces a new Semantic Governance suite, including the `SemanticGovernancePolicyEngine` singleton and `SemanticGovernancePolicies` resource for managing AI behavior. Developers should note several breaking changes: `skills.create` now requires a `skillId`, and the `interactions.delete` method has been moved to a location-scoped path. Additionally, the `AudioResponseFormat` and `ImageResponseFormat` schemas have renamed the `URL` enum value to `URI`. The API is also being rebranded in documentation from 'Vertex AI' to 'Agent Platform' or 'Gemini Enterprise Agent Platform' across several resource descriptions.

Other notable changes include the renaming of the `mcp` tool type to `mcp_server` in `AgentTool` and the addition of Hyperdisk support (e.g., `hyperdisk-ml`, `hyperdisk-balanced`) in `PersistentDiskSpec` for more performant storage options.

**Tags:** `governance` `agents` `breaking-change` `storage`
