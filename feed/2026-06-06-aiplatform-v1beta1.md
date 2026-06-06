---
date: 2026-06-06
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance arrives and Agent Platform rebrands"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Breaking Change"]
interesting_score: 9
---

# Semantic Governance arrives and Agent Platform rebrands

**Date:** 2026-06-06  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance framework and migrates several Agent-related resources. This update includes multiple breaking changes to resource paths, required fields, and enum values.

## Details

A new suite of Semantic Governance tools has been added, including `SemanticGovernancePolicyEngine` (a singleton resource) and `SemanticGovernancePolicies` for managing AI behavior. Significant breaking changes include: 1) `skillId` is now a required parameter in `skills.create`; 2) the `interactions` resource has been moved from the root to a location-nested path (`projects.locations.interactions`); 3) the `URL` enum value in `AudioResponseFormat` and `ImageResponseFormat` has been renamed to `URI`. Additionally, the API documentation reflects a shift in branding from 'Vertex AI' to 'Agent Platform' for several sub-services, and `PersistentDiskSpec` now supports various Hyperdisk types.

**Tags:** `AI` `Vertex AI` `Governance` `Breaking Change`
