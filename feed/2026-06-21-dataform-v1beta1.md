---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces native table-update triggers"
impact: medium
breaking: false
tags: ["data-engineering", "automation", "bigquery", "git"]
interesting_score: 8
---

# Dataform introduces native table-update triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports event-driven workflow execution, allowing workflows to trigger automatically when specific tables are updated.

## Details

This update introduces a robust triggering system via the new `WorkflowTriggerConfig` schema added to `WorkflowConfig`. Developers can now define `TableUpdateTrigger` objects to monitor specific tables for changes. The configuration includes sophisticated controls like `minExecutionDuration` (to throttle executions), `maxWaitDuration`, and logical conditions (`ALL` or `ANY`). Additionally, `GitRemoteSettings` now includes `gitRepositoryLink`, enabling the use of machine credentials via the standard `gitRepositoryLinks` resource format.

**Tags:** `data-engineering` `automation` `bigquery` `git`
