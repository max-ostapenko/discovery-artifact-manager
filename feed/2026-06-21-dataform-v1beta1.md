---
date: 2026-06-21
api: dataform.v1beta1
service: Dataform
title: "Dataform introduces event-driven workflow triggers"
impact: medium
breaking: false
tags: ["automation", "workflows", "git", "data-engineering"]
interesting_score: 7
---

# Dataform introduces event-driven workflow triggers

**Date:** 2026-06-21  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports automated workflow invocation via TableUpdateTriggers and adds a new GitRepositoryLink for machine credentials.

## Details

The API adds a comprehensive WorkflowTriggerConfig schema to WorkflowConfig, enabling workflows to fire automatically when specific tables are updated. This includes sophisticated controls like 'ALL' or 'ANY' condition logic, minExecutionDuration for throttling, and maxWaitDuration. Additionally, GitRemoteSettings now supports gitRepositoryLink, allowing developers to use standardized connection resources for machine-based Git authentication.

**Tags:** `automation` `workflows` `git` `data-engineering`
