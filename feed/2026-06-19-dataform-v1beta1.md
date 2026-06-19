---
date: 2026-06-19
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: medium
breaking: false
tags: ["automation", "data-pipelines", "git", "workflow"]
interesting_score: 7
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-19  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports automated workflow execution triggered by table updates, moving beyond manual or scheduled runs.

## Details

The API adds a comprehensive triggering system via the new `WorkflowTriggerConfig` schema. Developers can now define `TableUpdateTrigger` objects within a `WorkflowConfig` to invoke workflows automatically when specific target tables are modified. The configuration supports complex logic through `condition` (ALL/ANY), and provides throttling controls like `minExecutionDuration` and `maxWaitDuration`. Additionally, `GitRemoteSettings` now includes a `gitRepositoryLink` field for managing machine credentials via standard GCP resource paths.

**Tags:** `automation` `data-pipelines` `git` `workflow`
