---
date: 2026-06-10
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "iam", "automation"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-10  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources for machine-based authentication, streamlining how workflows connect to external Git providers.

## Details

The `GitRemoteSettings` schema has been updated with an optional `gitRepositoryLink` field. This field allows developers to reference a centralized connection resource (formatted as `projects/*/locations/*/connections/*/gitRepositoryLinks/*`) for authentication. This change facilitates better integration with Google Cloud's developer connection services, moving away from manual secret management for Git operations.

**Tags:** `dataform` `git` `iam` `automation`
