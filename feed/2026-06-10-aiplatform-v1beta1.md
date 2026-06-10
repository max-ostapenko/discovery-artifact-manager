---
date: 2026-06-10
api: aiplatform.v1beta1
service: Vertex AI
title: "Vertex AI adds Semantic Governance and MCP Agent Tools"
impact: high
breaking: true
tags: ["AI", "Governance", "Agents", "Breaking Change"]
interesting_score: 9
---

# Vertex AI adds Semantic Governance and MCP Agent Tools

**Date:** 2026-06-10  
**API:** `aiplatform.v1beta1`  
**Impact:** High  
**⚠️ Breaking change**  

## Summary

This update introduces a new Semantic Governance framework for policy management and significantly expands the Agent ecosystem with support for Model Context Protocol (MCP) servers.

## Details

A major new feature set, Semantic Governance, has been added via the `SemanticGovernancePolicyEngine` (a singleton resource) and `SemanticGovernancePolicies`. This allows for structured policy enforcement across AI resources. The Agent framework sees a significant upgrade, notably adding `mcp_server` as a tool type, allowing agents to interface with external tools using the Model Context Protocol. Additionally, infrastructure specs for `PersistentDiskSpec` now support various Hyperdisk types (e.g., `hyperdisk-ml`, `hyperdisk-balanced`) for high-performance workloads. 

Several breaking changes are included: the `skillId` parameter in `skills.create` is now required rather than optional. In the `GenaiVertexV1beta1` schemas for audio and image response formats, the enum value `URL` has been renamed to `URI`. Furthermore, the `interactions.delete` method has been moved under the project/location hierarchy, and several fields in `ReasoningEngines` memories are now explicitly marked as immutable during patch operations.

**Tags:** `AI` `Governance` `Agents` `Breaking Change`
