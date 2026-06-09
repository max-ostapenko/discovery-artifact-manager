---
date: 2026-06-09
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "auth", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-09  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports `gitRepositoryLink` in `GitRemoteSettings`, allowing developers to use centralized connection resources for Git authentication.

## Details

The `GitRemoteSettings` schema has been updated with a new optional field: `gitRepositoryLink`. This field accepts a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. This change enables the use of machine credentials managed via Git repository links, streamlining how Dataform interacts with remote repositories and potentially simplifying secret management.

**Tags:** `dataform` `git` `auth` `devops`
