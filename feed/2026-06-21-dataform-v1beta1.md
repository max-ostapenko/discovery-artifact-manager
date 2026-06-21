---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: medium
breaking: false
tags: ["data-pipelines", "automation", "bigquery", "git"]
interesting_score: 8
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform workflows can now be triggered automatically based on table updates, moving beyond manual or scheduled executions. New configuration schemas allow for complex trigger logic, including execution throttling and multi-condition evaluations.

## Details

The addition of `WorkflowTriggerConfig` to the `WorkflowConfig` resource enables automated workflow invocations. Developers can now define `TableUpdateTrigger` objects to watch specific tables for changes. The configuration supports logical conditions (`ALL` or `ANY` triggers), `minExecutionDuration` to throttle frequent updates, and `maxWaitDuration` to manage trigger timeouts. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, allowing for more streamlined machine credential management via resource names.

**Tags:** `data-pipelines` `automation` `bigquery` `git`
