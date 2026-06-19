---
date: 2026-06-19
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: high
breaking: false
tags: ["automation", "data-pipelines", "workflow-orchestration"]
interesting_score: 8
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-19  
**API:** `dataform.v1beta1`  
**Impact:** High  

## Summary

Dataform workflows can now be triggered automatically based on table updates, moving away from purely manual or external scheduling.

## Details

The API adds a comprehensive triggering system via the `workflowTriggerConfig` field in `WorkflowConfig`. This includes `TableUpdateTrigger`, which allows workflows to fire when specific tables are modified. Developers can configure complex logic using `condition` (ALL/ANY), `maxWaitDuration`, and `minExecutionDuration` to throttle executions. Additionally, a new `gitRepositoryLink` field in `GitRemoteSettings` allows for cleaner machine credential management via standard GCP connection resources.

**Tags:** `automation` `data-pipelines` `workflow-orchestration`
