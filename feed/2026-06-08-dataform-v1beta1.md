---
date: 2026-06-08
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-08  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking Git repositories via standardized connection resources, improving how machine credentials are managed for SQL workflows.

## Details

The `GitRemoteSettings` schema now includes a `gitRepositoryLink` field. This allows developers to point to a specific connection resource (formatted as `projects/*/locations/*/connections/*/gitRepositoryLinks/*`) for machine-based Git authentication. This update facilitates better integration with Google Cloud's centralized connection management, offering a more structured alternative to manual credential handling.

**Tags:** `dataform` `git` `security` `devops`
