---
date: 2026-05-30
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Breaking Skill ID Changes"
impact: high
breaking: true
tags: ["governance", "breaking-change", "agents", "storage"]
interesting_score: 8
---

# Semantic Governance and Breaking Skill ID Changes

**Date:** 2026-05-30  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and adds Hyperdisk support, while introducing breaking changes to Skill creation and response format enums.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicy resources for managing AI governance at the location level. A significant breaking change was made to the `projects.locations.skills.create` method, where `skillId` is now a required parameter. Additionally, the `delivery` enum in `AudioResponseFormat` and `ImageResponseFormat` has changed the value `URL` to `URI`. Developers using Agent Tools should note that the `mcp` type has been renamed to `mcp_server`. On the infrastructure side, `PersistentDiskSpec` now supports various Hyperdisk types, including `hyperdisk-balanced`, `hyperdisk-ml`, and `hyperdisk-throughput`.

**Tags:** `governance` `breaking-change` `agents` `storage`
