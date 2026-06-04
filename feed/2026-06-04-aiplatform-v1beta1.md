---
date: 2026-06-04
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Hyperdisk support"
impact: high
breaking: true
tags: ["governance", "agents", "infrastructure", "breaking-change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and Hyperdisk support

**Date:** 2026-06-04  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance framework for AI policy management and expands infrastructure options with Hyperdisk support, alongside several breaking API changes.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicies` resources, allowing developers to manage AI governance at the location level. The `PersistentDiskSpec` schema has been significantly expanded to support high-performance Hyperdisk types, including `hyperdisk-ml`, `hyperdisk-balanced`, and `hyperdisk-throughput`. 

Several breaking changes are included in this revision: 
1. The `skillId` parameter in `projects.locations.skills.create` is now **Required** (previously Optional).
2. In `AgentTool`, the tool type `mcp` has been renamed to `mcp_server`.
3. The `AudioResponseFormat` and `ImageResponseFormat` enums changed the value `URL` to `URI`.
4. Pagination for listing agents now enforces a maximum `pageSize` of 100 and a default of 10.

**Tags:** `governance` `agents` `infrastructure` `breaking-change`
