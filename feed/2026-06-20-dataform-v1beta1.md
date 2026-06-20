---
date: 2026-06-20
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: medium
breaking: false
tags: ["automation", "data-pipelines", "git", "events"]
interesting_score: 8
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-20  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports automated workflow execution triggered by table updates, moving beyond manual or scheduled runs.

## Details

The API adds a comprehensive triggering system via the new `WorkflowTriggerConfig` schema in `WorkflowConfig`. Developers can now define `TableUpdateTrigger` objects to invoke workflows when specific tables are modified. The system supports complex logic including 'ANY' or 'ALL' conditions, `minExecutionDuration` for debouncing, and `maxWaitDuration`. Additionally, `GitRemoteSettings` now includes a `gitRepositoryLink` field, allowing for standardized machine credential management via GCP resource names.

**Tags:** `automation` `data-pipelines` `git` `events`
