---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: high
breaking: false
tags: ["automation", "data-pipelines", "git", "bigquery"]
interesting_score: 8
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** High  

## Summary

Dataform workflows can now be triggered automatically by table updates, moving beyond manual or scheduled execution.

## Details

This update introduces a significant automation layer to Dataform. The new `WorkflowTriggerConfig` allows developers to define `TableUpdateTrigger` conditions, enabling workflows to fire when specific target tables are modified. It includes sophisticated controls like `minExecutionDuration` to prevent rapid-fire executions and `maxWaitDuration` for timeout logic. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, allowing for standardized machine credential management via Google Cloud's repository connection resources.

**Tags:** `automation` `data-pipelines` `git` `bigquery`
