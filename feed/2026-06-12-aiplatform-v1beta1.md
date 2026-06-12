---
date: 2026-06-12
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and MCP Tool Support"
impact: high
breaking: true
tags: ["AI", "Vertex AI", "Governance", "Agents", "Infrastructure"]
interesting_score: 9
---

# Vertex AI adds Semantic Governance and MCP Tool Support

**Date:** 2026-06-12  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

Vertex AI (v1beta1) introduces a new Semantic Governance framework for policy management and expands Agent capabilities with Model Context Protocol (MCP) support, alongside several breaking changes to resource paths and required fields.

## Details

This update introduces the SemanticGovernancePolicyEngine and SemanticGovernancePolicy resources, enabling structured AI policy enforcement and governance. The Agent framework receives a significant boost with support for 'mcp_server' tool types, allowing standardized integration with external data sources. Infrastructure-wise, PersistentDiskSpec now supports Hyperdisk types (balanced, extreme, throughput) for high-performance workloads. Developers should note several breaking changes: the 'skillId' parameter in the skills.create method is now required, and the 'Interactions' resource has been moved from a top-level resource to a location-based path. Additionally, enum values for audio and image delivery formats have transitioned from 'URL' to 'URI'.

**Tags:** `AI` `Vertex AI` `Governance` `Agents` `Infrastructure`
