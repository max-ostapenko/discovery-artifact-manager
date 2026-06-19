---
date: 2026-06-19
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven table update triggers"
impact: high
breaking: false
tags: ["data-engineering", "automation", "pipelines"]
interesting_score: 8
---

# Dataform introduces event-driven table update triggers

**Date:** 2026-06-19  
**API:** `dataform.v1beta1`  
**Impact:** High  

## Summary

Dataform workflows can now be automatically triggered by table updates, moving beyond manual or scheduled executions. New configuration schemas allow for complex triggering logic, including multi-condition requirements and execution throttling.

## Details

The API adds a comprehensive triggering system via `WorkflowTriggerConfig`. Developers can now define `TableUpdateTrigger` objects within `WorkflowConfig` to invoke workflows when specific tables are modified. The system supports logical conditions (`ALL` or `ANY`), `maxWaitDuration` for condition matching, and `minExecutionDuration` to prevent rapid-fire re-executions. Additionally, `GitRemoteSettings` now supports `gitRepositoryLink`, allowing developers to use standardized GCP Git repository resources for machine credentials instead of manual secret management.

**Tags:** `data-engineering` `automation` `pipelines`
