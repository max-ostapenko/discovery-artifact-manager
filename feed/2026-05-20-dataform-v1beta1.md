---
date: 2026-05-20
api: dataform.v1beta1
service: Dataform
title: "Asynchronous repository deletion and Git branch improvements"
impact: medium
breaking: false
tags: ["dataform", "git", "ops"]
interesting_score: 6
---

# Asynchronous repository deletion and Git branch improvements

**Date:** 2026-05-20  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform introduces long-running repository deletion and clarifies Git default branch behavior.

## Details

A new method `repositories.deleteLongRunning` has been added, allowing developers to delete repositories asynchronously. This includes a `force` parameter in the `DeleteRepositoryLongRunningRequest` to automatically clean up child resources like compilation results and workflow invocations, though it notably fails if workspaces or configs still exist. Additionally, `GitRemoteSettings.defaultBranch` is now optional (defaulting to 'main'), and a new output-only `effectiveDefaultBranch` field helps identify the active branch being used by the service.

**Tags:** `dataform` `git` `ops`
