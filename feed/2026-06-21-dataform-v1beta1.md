---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces table-driven workflow triggers"
impact: medium
breaking: false
tags: ["data-engineering", "automation", "workflow-orchestration"]
interesting_score: 8
---

# Dataform introduces table-driven workflow triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports automated workflow execution triggered by table updates, moving beyond manual or scheduled runs. New configuration options allow for complex trigger logic, including execution frequency limits and multi-condition evaluation.

## Details

The primary addition is the `WorkflowTriggerConfig` object within `WorkflowConfig`, which enables event-driven workflows. Developers can now use `TableUpdateTrigger` to start a workflow when a specific target table is modified. The configuration supports logical conditions (`ALL` or `ANY` triggers), `minExecutionDuration` to rate-limit invocations, and `maxWaitDuration`. Additionally, `GitRemoteSettings` now includes `gitRepositoryLink`, allowing for more robust machine credential management via resource names rather than just raw secrets.

**Tags:** `data-engineering` `automation` `workflow-orchestration`
