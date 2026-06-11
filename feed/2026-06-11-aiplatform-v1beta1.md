---
date: 2026-06-11
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI introduces Semantic Governance and Agent Platform"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 8
---

# Vertex AI introduces Semantic Governance and Agent Platform

**Date:** 2026-06-11  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) has introduced a Semantic Governance Policy Engine and shifted branding toward 'Agent Platform.' This update includes significant breaking changes to resource IDs, tool types, and media delivery enums.

## Details

A new Semantic Governance suite has been added, featuring a singleton SemanticGovernancePolicyEngine (with GET/PATCH upsert) and SemanticGovernancePolicies. The Agent resource has been refined with stricter ID validation and a terminology shift from 'Vertex AI' to 'Agent Platform' in many descriptions. Developers using Model Context Protocol (MCP) tools should note the type rename from 'mcp' to 'mcp_server'. Additionally, PersistentDiskSpec now supports a wide array of Hyperdisk types including hyperdisk-ml and hyperdisk-throughput.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
