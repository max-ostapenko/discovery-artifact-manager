---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces native table-update triggers"
impact: medium
breaking: false
tags: ["automation", "data-engineering", "git", "workflow"]
interesting_score: 8
---

# Dataform introduces native table-update triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports automated workflow execution triggered by table updates, reducing the need for external orchestrators.

## Details

The API adds a comprehensive triggering system via `WorkflowTriggerConfig` within `WorkflowConfig`. Developers can now define `TableUpdateTrigger` objects to invoke workflows automatically when specific tables are modified. The configuration supports complex logic including 'ALL' or 'ANY' conditions, execution throttling via `minExecutionDuration`, and observability through `recentTriggerEvaluationRecords`. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink` for managing machine credentials using standard GCP resource paths.

**Tags:** `automation` `data-engineering` `git` `workflow`
