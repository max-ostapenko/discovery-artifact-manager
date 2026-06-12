---
date: 2026-06-12
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "iam", "credentials"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-12  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports `gitRepositoryLink` in Git remote settings, allowing developers to use centralized machine credentials for repository connections.

## Details

The `GitRemoteSettings` schema has been updated with a new optional field: `gitRepositoryLink`. This field accepts a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`, enabling more robust integration with Google Cloud's connection management for Git-based workflows instead of relying solely on manual token configurations.

**Tags:** `dataform` `git` `iam` `credentials`
