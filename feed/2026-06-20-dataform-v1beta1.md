---
date: 2026-06-20
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: medium
breaking: false
tags: ["automation", "workflows", "git", "data-engineering"]
interesting_score: 7
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-20  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform workflows can now be triggered automatically based on table updates, moving beyond manual or scheduled executions.

## Details

The API adds a robust triggering system via `WorkflowTriggerConfig` and `TableUpdateTrigger`. Developers can now configure workflows to execute when specific tables are updated, using logic gates like `ANY` or `ALL` conditions. New fields like `minExecutionDuration` and `maxWaitDuration` provide rate-limiting and timeout controls for these automated runs. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, allowing for more standardized machine credential management using Google Cloud resource paths.

**Tags:** `automation` `workflows` `git` `data-engineering`
