---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven table update triggers"
impact: high
breaking: false
tags: ["automation", "data-pipelines", "triggers", "git"]
interesting_score: 8
---

# Dataform introduces event-driven table update triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** High  

## Summary

Dataform workflows can now be triggered automatically based on table updates, moving beyond manual or scheduled executions. New configuration options allow for complex trigger logic, including execution throttling and evaluation history.

## Details

The addition of `WorkflowTriggerConfig` to `WorkflowConfig` enables automated workflow invocation. The primary new trigger type is `TableUpdateTrigger`, which monitors a specific target table for changes. Developers can now define sophisticated triggering logic using the `condition` field (supporting `ALL` or `ANY` triggers), `minExecutionDuration` for throttling, and `maxWaitDuration` for timeouts. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, allowing machine credentials to be managed via standardized resource names.

**Tags:** `automation` `data-pipelines` `triggers` `git`
