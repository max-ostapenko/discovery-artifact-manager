---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: medium
breaking: false
tags: ["data-engineering", "automation", "workflows"]
interesting_score: 8
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports automated workflow execution triggered by table updates, moving beyond manual or scheduled runs.

## Details

The API adds a comprehensive `WorkflowTriggerConfig` to the `WorkflowConfig` resource. This includes `TableUpdateTrigger`, which allows developers to invoke workflows automatically when a specific target table is modified. The configuration supports complex logic via `condition` (ALL/ANY), and provides execution throttling through `minExecutionDuration` and `maxWaitDuration`. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink` for more robust machine credential management using standard GCP connection resources.

**Tags:** `data-engineering` `automation` `workflows`
