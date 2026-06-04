---
date: 2026-06-04
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives alongside breaking Agent changes"
impact: high
breaking: true
tags: ["governance", "agents", "infrastructure", "breaking-change"]
interesting_score: 8
---

# Semantic Governance arrives alongside breaking Agent changes

**Date:** 2026-06-04  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance framework for location-based policy management, while introducing breaking changes to the Agents and Skills APIs.

## Details

This update introduces the `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicy` resources, allowing developers to manage AI governance at the location level. However, there are several breaking changes in this beta revision: the `skillId` parameter in `skills.create` is now required rather than optional, and the `AgentTool` type `mcp` has been renamed to `mcp_server`. Additionally, `PersistentDiskSpec` has been expanded to support various Hyperdisk types (including `hyperdisk-ml` and `hyperdisk-balanced`), and GenAI response formats for audio and images have transitioned from `URL` to `URI` terminology.

**Tags:** `governance` `agents` `infrastructure` `breaking-change`
