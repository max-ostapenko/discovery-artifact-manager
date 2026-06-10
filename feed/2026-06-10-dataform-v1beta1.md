---
date: 2026-06-10
api: dataform.v1beta1
service: Dataform
title: "Dataform adds GitRepositoryLink for machine credentials"
impact: medium
breaking: false
tags: ["dataform", "git", "security", "devops"]
interesting_score: 5
---

# Dataform adds GitRepositoryLink for machine credentials

**Date:** 2026-06-10  
**API:** `dataform.v1beta1`  
**Impact:** Medium  

## Summary

Dataform now supports linking to GitRepositoryLink resources for machine-based authentication, streamlining how workspaces connect to remote repositories.

## Details

The GitRemoteSettings schema has been updated to include a new optional field: gitRepositoryLink. This field accepts a resource name in the format projects/*/locations/*/connections/*/gitRepositoryLinks/*, allowing developers to leverage centralized Google Cloud Git connections for machine credentials instead of managing secrets manually within Dataform.

**Tags:** `dataform` `git` `security` `devops`
