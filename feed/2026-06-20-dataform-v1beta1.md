---
date: 2026-06-20
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: medium
breaking: false
tags: ["automation", "data-pipelines", "git", "events"]
interesting_score: 7
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-20  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports triggering workflows based on table updates, enabling more reactive data pipelines. A new Git repository link field also simplifies machine credential management.

## Details

The API adds a comprehensive triggering system via `WorkflowTriggerConfig` on the `WorkflowConfig` resource. This includes `TableUpdateTrigger` for monitoring specific table changes, and configuration options like `minExecutionDuration` (to throttle executions) and `maxWaitDuration`. Developers can also track the health of these triggers through `TriggerEvaluationRecord`. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, allowing for standardized resource-based machine credentials.

**Tags:** `automation` `data-pipelines` `git` `events`
