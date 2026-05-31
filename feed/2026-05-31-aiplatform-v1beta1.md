---
date: 2026-05-31
api: aiplatform.v1beta1
service: Vertex AI
title: "New Semantic Governance and Breaking Changes to Skills/Agents"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "compute"]
interesting_score: 8
---

# New Semantic Governance and Breaking Changes to Skills/Agents

**Date:** 2026-05-31  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a Semantic Governance Policy Engine while making breaking changes to Skill creation and Agent Tool definitions.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicies resources for managing AI governance at the location level. Crucially, several breaking changes were introduced: the `skillId` parameter in `projects.locations.skills.create` is now Required, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, the `PersistentDiskSpec` schema now supports Hyperdisk types (balanced, extreme, ML, and throughput), and Agent list operations now default to a page size of 10 with a hard limit of 100.

**Tags:** `governance` `agents` `breaking-change` `compute`
