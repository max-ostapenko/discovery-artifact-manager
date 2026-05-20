---
date: 2026-05-20
api: dataform.v1beta1
service: Dataform
title: "Dataform adds asynchronous repository deletion"
impact: medium
breaking: false
tags: ["dataform", "bigquery", "git-integration"]
interesting_score: 6
---

# Dataform adds asynchronous repository deletion

**Date:** 2026-05-20  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports long-running repository deletions and relaxes requirements for Git default branches.

## Details

A new `deleteLongRunning` method has been added to the repositories resource, allowing for asynchronous cleanup. This includes a `DeleteRepositoryLongRunningRequest` with a `force` flag to purge child resources like compilation results and workflow invocations. On the Git integration side, `GitRemoteSettings.defaultBranch` is now optional rather than required, and a new output-only `effectiveDefaultBranch` field helps developers identify the resolved branch name (defaulting to 'main').

**Tags:** `dataform` `bigquery` `git-integration`
