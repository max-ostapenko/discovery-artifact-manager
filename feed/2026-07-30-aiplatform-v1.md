---
date: 2026-07-30
api: aiplatform.v1
service: Vertex AI
title: "Vertex AI adds Compact HTTP Forwarding and Serving Profile Ops"
impact: medium
breaking: false
tags: ["AI", "Vertex AI", "Model Serving", "Operations"]
interesting_score: 6
---

# Vertex AI adds Compact HTTP Forwarding and Serving Profile Ops

**Date:** 2026-07-30  
**API:** `aiplatform.v1`  
**Impact:** Medium  

## Summary

Vertex AI introduces a new 'compact' method for HTTP request forwarding to publisher endpoints and adds full lifecycle management for operations under Serving Profiles.

## Details

Developers can now use the `projects.locations.publishers.v1.responses.compact` method to forward arbitrary POST requests (using `GoogleApiHttpBody`) to specific deployed models. This is particularly useful for custom proxying or streaming scenarios where an `invoke_route_prefix` is configured. Additionally, the `servingProfiles` resource now includes a dedicated `operations` sub-resource, providing standard `get`, `list`, `cancel`, and `delete` methods for tracking and managing long-running tasks associated with serving configurations. A minor documentation update also clarifies that durations in the `OnlineEvaluator` trace scope are measured in seconds.

**Tags:** `AI` `Vertex AI` `Model Serving` `Operations`
