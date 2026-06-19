---
date: 2026-06-19
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces native table-update workflow triggers"
impact: medium
breaking: false
tags: ["automation", "data-pipelines", "git", "event-driven"]
interesting_score: 8
---

# Dataform introduces native table-update workflow triggers

**Date:** 2026-06-19  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform workflows can now be triggered automatically based on table updates, moving beyond manual or scheduled execution. The update also improves Git credential management via a new repository link field.

## Details

The API adds a comprehensive triggering system via the `WorkflowTriggerConfig` schema. Developers can now define `TableUpdateTrigger` objects to invoke workflows when specific tables are modified. This includes sophisticated control over execution logic, such as `condition` (ALL/ANY triggers), `minExecutionDuration` for throttling, and `maxWaitDuration`. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, allowing for more standardized machine credential management using GCP resource names. Observability is also improved with `TriggerEvaluationRecord`, which tracks the success or failure of the last 10 trigger evaluations.

**Tags:** `automation` `data-pipelines` `git` `event-driven`
