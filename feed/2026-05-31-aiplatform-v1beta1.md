---
date: 2026-05-31
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and breaks Skill IDs"
impact: high
breaking: true
tags: ["Vertex AI", "Governance", "Generative AI", "Breaking Change"]
interesting_score: 8
---

# Vertex AI adds Semantic Governance and breaks Skill IDs

**Date:** 2026-05-31  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI introduces a new Semantic Governance Policy Engine and associated policies, alongside infrastructure updates for Hyperdisks and several breaking API changes.

## Details

This update introduces the SemanticGovernancePolicyEngine (a singleton resource) and SemanticGovernancePolicies for managing AI governance at the project/location level. Infrastructure-wise, PersistentDiskSpec now supports various Hyperdisk types including Balanced, Extreme, ML, and Throughput. Developers must address two breaking changes: the skillId parameter in skills.create is now Required (previously Optional), and the AgentTool type 'mcp' has been renamed to 'mcp_server'. Additionally, agents.list pagination has been updated with a new default page size of 10 and a maximum of 100.

**Tags:** `Vertex AI` `Governance` `Generative AI` `Breaking Change`
