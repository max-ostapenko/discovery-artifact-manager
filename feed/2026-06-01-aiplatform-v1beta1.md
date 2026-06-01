---
date: 2026-06-01
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and Hyperdisk support"
impact: high
breaking: true
tags: ["governance", "genai", "storage", "breaking-change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and Hyperdisk support

**Date:** 2026-06-01  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework for policy management and expands storage options with Hyperdisk support, while introducing several breaking changes to existing schemas.

## Details

A new suite of methods for `SemanticGovernancePolicyEngine` and `SemanticGovernancePolicy` has been added, allowing developers to manage AI governance at the location level. Notably, the `skills.create` method now requires a `skillId`, which was previously optional. In the GenAI response formats for audio and images, the delivery enum value `URL` has been renamed to `URI`, which will break integrations relying on the specific string value. Additionally, `PersistentDiskSpec` now supports a wide array of Hyperdisk types, including `hyperdisk-balanced`, `hyperdisk-extreme`, and `hyperdisk-ml`. The Agent API also received significant documentation refinement and stricter validation for resource IDs.

**Tags:** `governance` `genai` `storage` `breaking-change`
