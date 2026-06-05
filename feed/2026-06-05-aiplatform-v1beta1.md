---
date: 2026-06-05
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Hyperdisk support arrive in Vertex AI"
impact: high
breaking: true
tags: ["AI", "Governance", "Breaking Change", "Infrastructure"]
interesting_score: 8
---

# Semantic Governance and Hyperdisk support arrive in Vertex AI

**Date:** 2026-06-05  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine and expands infrastructure options with Hyperdisk support, alongside several breaking changes to Agents and Skills.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies, providing a new framework for managing AI guardrails via singleton resources. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now required, and the Agent tool type `mcp` has been renamed to `mcp_server`. Additionally, response formats for audio and images have transitioned from `URL` to `URI` enums. On the infrastructure side, `PersistentDiskSpec` now supports a wide array of Hyperdisk types, including `hyperdisk-ml` and `hyperdisk-throughput`. There is also a notable documentation shift, with many 'Vertex AI' references being rebranded to 'Agent Platform'.

**Tags:** `AI` `Governance` `Breaking Change` `Infrastructure`
