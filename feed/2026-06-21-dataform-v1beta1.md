---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces Table Update Triggers and Git Links"
impact: high
breaking: false
tags: ["dataform", "automation", "git", "bigquery"]
interesting_score: 8
---

# Dataform introduces Table Update Triggers and Git Links

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** High  

## Summary

Dataform workflows can now be triggered automatically by table updates, moving closer to a fully event-driven data orchestration model.

## Details

This update introduces `WorkflowTriggerConfig`, a significant addition to `WorkflowConfig` that allows for automated execution. The standout feature is `TableUpdateTrigger`, which enables workflows to start when a specific target table is modified. Developers can fine-tune these triggers using `minExecutionDuration` to throttle executions and `maxWaitDuration` to set timeouts. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, allowing for more streamlined machine credential management via standardized resource names.

**Tags:** `dataform` `automation` `git` `bigquery`
