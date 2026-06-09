---
date: 2026-06-09
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "authentication", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-09  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources for machine-based authentication in GitRemoteSettings.

## Details

The `GitRemoteSettings` schema has been updated with a new optional field: `gitRepositoryLink`. This field allows developers to provide a resource name in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*` to manage machine credentials. This addition facilitates better integration with GCP's centralized connection management for Git-based workflows.

**Tags:** `dataform` `git` `authentication` `devops`
