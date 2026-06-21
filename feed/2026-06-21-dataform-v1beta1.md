---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: high
breaking: false
tags: ["dataform", "automation", "workflows", "git"]
interesting_score: 8
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** High  

## Summary

Dataform now supports triggering workflows automatically based on table updates and adds improved Git credential management.

## Details

A significant update to the WorkflowConfig schema introduces `workflowTriggerConfig`, allowing developers to define automated triggers. The primary new trigger type is `TableUpdateTrigger`, which invokes a workflow when a specific target table is modified. Developers can now control execution flow using `minExecutionDuration` to throttle frequent updates and `maxWaitDuration` to set timeouts for trigger conditions. Additionally, `GitRemoteSettings` now includes `gitRepositoryLink`, enabling the use of machine credentials via the `gitRepositoryLinks` resource for more secure and standardized Git integrations.

**Tags:** `dataform` `automation` `workflows` `git`
