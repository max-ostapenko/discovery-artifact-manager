---
date: 2026-06-11
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and refactors Agent API"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and refactors Agent API

**Date:** 2026-06-11  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance Policy Engine and enforces stricter requirements for Skill creation, alongside a terminology shift toward 'Agent Platform'.

## Details

This update introduces the `SemanticGovernancePolicyEngine`, a singleton resource for managing AI policies at the location level, including a new `update` method that performs an upsert. Developers should note several breaking changes: the `skillId` parameter in `skills.create` is now Required (previously Optional), and the `delivery` enum values in `AudioResponseFormat` and `ImageResponseFormat` have been renamed from `URL` to `URI`. Additionally, the default `pageSize` for listing agents has been reduced from 100 to 10, and the `interactions.delete` method has been moved under the location-scoped resource path.

**Tags:** `governance` `agents` `breaking-change`
