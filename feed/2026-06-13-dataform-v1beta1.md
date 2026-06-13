---
date: 2026-06-13
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine auth"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine auth

**Date:** 2026-06-13  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports `gitRepositoryLink` in Git remote settings, enabling machine-based authentication via centralized connection resources.

## Details

The `GitRemoteSettings` schema has been expanded with an optional `gitRepositoryLink` field. This field accepts a resource path following the `projects/*/locations/*/connections/*/gitRepositoryLinks/*` pattern. This addition facilitates better integration with Google Cloud's connection management services, allowing for more secure and manageable machine-to-Git credentials instead of relying solely on manual secret management.

**Tags:** `dataform` `git` `security` `devops`
