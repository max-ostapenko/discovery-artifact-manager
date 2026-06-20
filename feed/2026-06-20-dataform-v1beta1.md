---
date: 2026-06-20
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: medium
breaking: false
tags: ["data-pipelines", "automation", "git", "bigquery"]
interesting_score: 8
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-20  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform workflows can now be automatically triggered by table updates, moving beyond manual or scheduled executions.

## Details

This update introduces a robust triggering system for Dataform. The new `WorkflowTriggerConfig` added to `WorkflowConfig` allows developers to define `TableUpdateTrigger` conditions, enabling workflows to execute when specific tables are modified. The system supports complex logic via `ALL` or `ANY` conditions, and provides execution controls like `minExecutionDuration` to prevent rapid-fire re-runs. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, facilitating better integration with machine credentials via standard Google Cloud repository connections.

**Tags:** `data-pipelines` `automation` `git` `bigquery`
