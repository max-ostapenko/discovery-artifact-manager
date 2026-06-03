---
date: 2026-06-03
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Hyperdisk support"
impact: high
breaking: true
tags: ["AI", "Governance", "Infrastructure", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and Hyperdisk support

**Date:** 2026-06-03  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine for managing AI guardrails and expands infrastructure options with Hyperdisk support. Several breaking changes affect Agent tools and Skill creation.

## Details

A new singleton resource, SemanticGovernancePolicyEngine, and associated SemanticGovernancePolicies have been added to manage AI governance at the location level. On the infrastructure side, PersistentDiskSpec now supports various Hyperdisk types, including hyperdisk-ml and hyperdisk-balanced. Note several breaking changes: the skillId parameter in the skills.create method is now required, and the AgentTool type 'mcp' has been renamed to 'mcp_server'. Additionally, ListAgents now defaults to a page size of 10 (down from 100), and GenAI response formats have transitioned from 'URL' to 'URI' terminology.

**Tags:** `AI` `Governance` `Infrastructure` `Breaking Change`
