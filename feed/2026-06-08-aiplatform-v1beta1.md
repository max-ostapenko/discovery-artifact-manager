---
date: 2026-06-08
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives and Agent API breaks"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Semantic Governance arrives and Agent API breaks

**Date:** 2026-06-08  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine while rolling out breaking changes to the Agents and Skills APIs, including required IDs and renamed tool types.

## Details

This update introduces the SemanticGovernancePolicyEngine, a singleton resource for managing AI guardrails via SemanticGovernancePolicies. Developers should note several breaking changes: the 'skillId' is now required when creating Skills, and the 'mcp' tool type in AgentTool has been renamed to 'mcp_server'. Additionally, the delivery enum for Audio and Image response formats has shifted from 'URL' to 'URI'. The PersistentDiskSpec schema has also been expanded to support various Hyperdisk types (balanced, extreme, ML, and throughput).

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
