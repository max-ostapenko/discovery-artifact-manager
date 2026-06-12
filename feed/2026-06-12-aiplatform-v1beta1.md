---
date: 2026-06-12
api: aiplatform.v1beta1
service: Vertex AI
title: "Semantic Governance and Interaction Resource Restructuring"
impact: high
breaking: true
tags: ["governance", "agents", "breaking-change", "infrastructure"]
interesting_score: 8
---

# Semantic Governance and Interaction Resource Restructuring

**Date:** 2026-06-12  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI v1beta1 introduces a new Semantic Governance framework and restructures the Interactions API, alongside several breaking schema changes.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicy resources for managing AI governance at the location level. Crucially, the 'interactions' resource has been moved from a top-level resource to a location-nested resource (e.g., projects.locations.interactions), which is a breaking change for existing integrations. Additionally, the 'skillId' parameter in the skills.create method is now required rather than optional. Infrastructure-wise, PersistentDiskSpec has been expanded to support Hyperdisk types including hyperdisk-ml and hyperdisk-throughput.

**Tags:** `governance` `agents` `breaking-change` `infrastructure`
